"""LearnSphere auth module (in-memory): sign up, OTP, login, session, Google."""
import hashlib
import re
import secrets
class AuthError(Exception):
    pass
class FakeGoogle:
    """Stands in for Google: gives one-time codes that expire in 5 minutes."""
    def __init__(self, clock):
        self.clock, self.codes = clock, {}
    def issue_code(self, email, name):
        code = secrets.token_hex(6)
        self.codes[code] = (email, name, self.clock() + 300)
        return code
    def exchange(self, code):
        if code not in self.codes:
            raise AuthError("invalid code")
        email, name, expiry = self.codes.pop(code)          # one time use only
        if self.clock() >= expiry:
            raise AuthError("code expired")
        return email, name
class Auth:
    def __init__(self, clock, google):
        self.clock, self.google = clock, google
        self.users, self.sessions, self.states, self.mailbox = {}, {}, set(), {}
    def _hash(self, pwd, salt):
        return hashlib.pbkdf2_hmac("sha256", pwd.encode(), salt, 1000).hex()
    def _session(self, email):
        token = secrets.token_hex(16)
        self.sessions[token] = (email, self.clock() + 1800)       # 30 minutes
        return token
    # ---------- sign up and e-mail OTP ----------
    def register(self, name, email, pwd, confirm):
        if not re.fullmatch(r"[A-Za-z ]{2,50}", name.strip()):
            raise AuthError("invalid name")
        if not re.fullmatch(r"[^@\s]+@[^@\s]+\.[A-Za-z]{2,}", email):
            raise AuthError("invalid email")
        email = email.lower()
        if email in self.users:
            raise AuthError("email already registered")
        rules = [len(pwd) >= 8, re.search("[A-Z]", pwd), re.search("[a-z]", pwd),
                 re.search(r"\d", pwd), re.search(r"\W", pwd)]
        if not all(rules):
            raise AuthError("weak password")
        if pwd != confirm:
            raise AuthError("passwords do not match")
        salt = secrets.token_bytes(8)
        self.users[email] = dict(name=name.strip(), salt=salt, verified=False,
                                 hash=self._hash(pwd, salt), fails=0,
                                 locked_until=0)
        self.send_otp(email)
    def send_otp(self, email):
        otp = str(secrets.randbelow(900000) + 100000)
        expiry = self.clock() + 300
        self.users[email].update(otp=otp, otp_expiry=expiry, otp_tries=0)
        self.mailbox[email] = otp                                  # "sent" by mail
    def verify(self, email, otp):
        user = self.users[email]
        if user["otp_tries"] >= 3:
            raise AuthError("too many attempts")
        if self.clock() >= user["otp_expiry"]:
            raise AuthError("otp expired")
        if otp != user["otp"]:
            user["otp_tries"] += 1
            raise AuthError("wrong otp")
        user["verified"] = True
    # ---------- login, session ----------
    def login(self, email, pwd):
        email = email.lower()
        user = self.users.get(email)
        if user is None:
            raise AuthError("invalid credentials")
        if self.clock() < user["locked_until"]:
            raise AuthError("account locked")
        if self._hash(pwd, user["salt"]) != user["hash"]:
            user["fails"] += 1
            if user["fails"] == 5:                           # lock for 15 minutes
                user["locked_until"], user["fails"] = self.clock() + 900, 0
            raise AuthError("invalid credentials")
        if not user["verified"]:
            raise AuthError("email not verified")
        user["fails"] = 0
        return self._session(email)
    def whoami(self, token):
        if token not in self.sessions:
            raise AuthError("invalid session")
        email, expiry = self.sessions[token]
        if self.clock() >= expiry:
            del self.sessions[token]
            raise AuthError("session expired")
        return self.users[email]["name"]
    def logout(self, token):
        self.sessions.pop(token, None)
    # ---------- Continue with Google (OAuth 2.0) ----------
    def google_start(self):
        state = secrets.token_hex(8)
        self.states.add(state)
        return state
    def google_callback(self, code, state):
        if state not in self.states:
            raise AuthError("invalid state")
        self.states.remove(state)                              # state works once
        email, name = self.google.exchange(code)
        self.users.setdefault(email, dict(name=name, salt=b"", hash="",
                                          verified=True, fails=0, locked_until=0))
        return self._session(email)
