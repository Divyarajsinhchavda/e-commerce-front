"""Practical 11: tests for learnsphere_auth.py (sign up, login, OAuth)."""
import unittest
from learnsphere_auth import Auth, AuthError, FakeGoogle
EMAIL, PWD = "riya.shah@gmail.com", "Learn@123"
GMAIL = "kunal.joshi@gmail.com"
class Clock:
    """Fake clock so that expiry can be tested without waiting."""
    def __init__(self):
        self.now = 1000.0
    def __call__(self):
        return self.now
    def move(self, seconds):
        self.now += seconds
class Base(unittest.TestCase):
    def setUp(self):
        self.clock = Clock()
        self.google = FakeGoogle(self.clock)
        self.auth = Auth(self.clock, self.google)
    def fails(self, message, func, *args):
        with self.assertRaises(AuthError) as error:
            func(*args)
        self.assertEqual(str(error.exception), message)
    def signup(self, verified=True):
        self.auth.register("Riya Shah", EMAIL, PWD, PWD)
        if verified:
            self.auth.verify(EMAIL, self.auth.mailbox[EMAIL])
class SignUp(Base):
    def test_01(self):
        """REG-01 Valid details are accepted"""
        self.signup(verified=False)
        self.assertFalse(self.auth.users[EMAIL]["verified"])
    def test_02(self):
        """REG-02 Duplicate e-mail is rejected"""
        self.signup(verified=False)
        self.fails("email already registered", self.auth.register,
                   "A B", EMAIL, PWD, PWD)
    def test_03(self):
        """REG-03 Duplicate e-mail in capital letters is rejected"""
        self.signup(verified=False)
        self.fails("email already registered", self.auth.register,
                   "A B", EMAIL.upper(), PWD, PWD)
    def test_04(self):
        """REG-04 E-mail without @ is rejected"""
        self.fails("invalid email", self.auth.register,
                   "Riya Shah", "riya.gmail.com", PWD, PWD)
    def test_05(self):
        """REG-05 Name with digits is rejected"""
        self.fails("invalid name", self.auth.register, "Riya123", EMAIL, PWD, PWD)
    def test_06(self):
        """REG-06 Password of 7 characters is rejected"""
        self.fails("weak password", self.auth.register,
                   "Riya Shah", EMAIL, "Lea@123", "Lea@123")
    def test_07(self):
        """REG-07 Password of exactly 8 characters is accepted"""
        self.auth.register("Riya Shah", EMAIL, "Learn@12", "Learn@12")
    def test_08(self):
        """REG-08 Password without special character is rejected"""
        self.fails("weak password", self.auth.register,
                   "Riya Shah", EMAIL, "Learn1234", "Learn1234")
    def test_09(self):
        """REG-09 Confirm password not matching is rejected"""
        self.fails("passwords do not match", self.auth.register,
                   "Riya Shah", EMAIL, PWD, "Learn@124")
    def test_10(self):
        """REG-10 Password is stored as hash, not plain text"""
        self.signup(verified=False)
        self.assertNotIn(PWD, str(self.auth.users[EMAIL]))
class OTP(Base):
    def setUp(self):
        super().setUp()
        self.signup(verified=False)
        self.otp = self.auth.mailbox[EMAIL]
    def test_01(self):
        """OTP-01 Correct OTP verifies the account"""
        self.auth.verify(EMAIL, self.otp)
        self.assertTrue(self.auth.users[EMAIL]["verified"])
    def test_02(self):
        """OTP-02 Wrong OTP is rejected"""
        self.fails("wrong otp", self.auth.verify, EMAIL, "000000")
    def test_03(self):
        """OTP-03 OTP still works at 299 seconds"""
        self.clock.move(299)
        self.auth.verify(EMAIL, self.otp)
    def test_04(self):
        """OTP-04 OTP expires at 300 seconds"""
        self.clock.move(300)
        self.fails("otp expired", self.auth.verify, EMAIL, self.otp)
    def test_05(self):
        """OTP-05 Blocked after 3 wrong attempts"""
        for _ in range(3):
            self.fails("wrong otp", self.auth.verify, EMAIL, "000000")
        self.fails("too many attempts", self.auth.verify, EMAIL, self.otp)
    def test_06(self):
        """OTP-06 Resent OTP works after the old one expired"""
        self.clock.move(400)
        self.auth.send_otp(EMAIL)
        self.auth.verify(EMAIL, self.auth.mailbox[EMAIL])
class Login(Base):
    def setUp(self):
        super().setUp()
        self.signup()
    def test_01(self):
        """LOG-01 Login with correct e-mail and password"""
        self.assertEqual(self.auth.whoami(self.auth.login(EMAIL, PWD)), "Riya Shah")
    def test_02(self):
        """LOG-02 Wrong password is rejected"""
        self.fails("invalid credentials", self.auth.login, EMAIL, "Wrong@123")
    def test_03(self):
        """LOG-03 Unknown e-mail gives the same error message"""
        self.fails("invalid credentials", self.auth.login, "nobody@gmail.com", PWD)
    def test_04(self):
        """LOG-04 E-mail is not case sensitive"""
        self.assertTrue(self.auth.login(EMAIL.upper(), PWD))
    def test_05(self):
        """LOG-05 Login without e-mail verification is rejected"""
        self.auth.register("Mehul Patel", "mehul@gmail.com", PWD, PWD)
        self.fails("email not verified", self.auth.login, "mehul@gmail.com", PWD)
    def test_06(self):
        """LOG-06 Account locks after 5 wrong passwords"""
        for _ in range(5):
            self.fails("invalid credentials", self.auth.login, EMAIL, "Wrong@123")
        self.fails("account locked", self.auth.login, EMAIL, PWD)
    def test_07(self):
        """LOG-07 4 wrong passwords then correct one works"""
        for _ in range(4):
            self.fails("invalid credentials", self.auth.login, EMAIL, "Wrong@123")
        self.assertTrue(self.auth.login(EMAIL, PWD))
    def test_08(self):
        """LOG-08 Locked account opens again after 15 minutes"""
        for _ in range(5):
            self.fails("invalid credentials", self.auth.login, EMAIL, "Wrong@123")
        self.clock.move(900)
        self.assertTrue(self.auth.login(EMAIL, PWD))
class Session(Base):
    def setUp(self):
        super().setUp()
        self.signup()
        self.token = self.auth.login(EMAIL, PWD)
    def test_01(self):
        """SES-01 Fake session token is rejected"""
        self.fails("invalid session", self.auth.whoami, "abc123")
    def test_02(self):
        """SES-02 Session is valid at 1799 seconds"""
        self.clock.move(1799)
        self.assertEqual(self.auth.whoami(self.token), "Riya Shah")
    def test_03(self):
        """SES-03 Session expires at 1800 seconds"""
        self.clock.move(1800)
        self.fails("session expired", self.auth.whoami, self.token)
    def test_04(self):
        """SES-04 Token cannot be used after logout"""
        self.auth.logout(self.token)
        self.fails("invalid session", self.auth.whoami, self.token)
class GoogleLogin(Base):
    def code(self):
        return self.google.issue_code(GMAIL, "Kunal Joshi")
    def test_01(self):
        """OA-01 Start gives a new state value"""
        self.assertIn(self.auth.google_start(), self.auth.states)
    def test_02(self):
        """OA-02 First Google login creates a verified account"""
        token = self.auth.google_callback(self.code(), self.auth.google_start())
        self.assertEqual(self.auth.whoami(token), "Kunal Joshi")
        self.assertTrue(self.auth.users[GMAIL]["verified"])
    def test_03(self):
        """OA-03 Existing user is not duplicated"""
        self.auth.register("Kunal Joshi", GMAIL, PWD, PWD)
        self.auth.google_callback(self.code(), self.auth.google_start())
        self.assertEqual(len(self.auth.users), 1)
    def test_04(self):
        """OA-04 Wrong state is rejected (CSRF check)"""
        self.auth.google_start()
        self.fails("invalid state", self.auth.google_callback,
                   self.code(), "fake-state")
    def test_05(self):
        """OA-05 Same state cannot be used twice"""
        state = self.auth.google_start()
        self.auth.google_callback(self.code(), state)
        self.fails("invalid state", self.auth.google_callback, self.code(), state)
    def test_06(self):
        """OA-06 Authorization code works only once"""
        code = self.code()
        self.auth.google_callback(code, self.auth.google_start())
        self.fails("invalid code", self.auth.google_callback,
                   code, self.auth.google_start())
    def test_07(self):
        """OA-07 Authorization code expires after 5 minutes"""
        state, code = self.auth.google_start(), self.code()
        self.clock.move(300)
        self.fails("code expired", self.auth.google_callback, code, state)
if __name__ == "__main__":
    groups = [("SIGN UP", SignUp), ("E-MAIL OTP", OTP), ("LOGIN", Login),
              ("SESSION", Session), ("GOOGLE OAUTH", GoogleLogin)]
    print("LEARNSPHERE AUTH MODULE - TEST REPORT")
    rows = []
    for title, cls in groups:
        print(f"\n{title}")
        passed = total = 0
        for test in unittest.defaultTestLoader.loadTestsFromTestCase(cls):
            result = unittest.TestResult()
            test.run(result)
            ok = "PASS" if result.wasSuccessful() else "FAIL"
            print(f"  {test.shortDescription():<62}{ok}")
            total += 1
            passed += result.wasSuccessful()
        rows.append((title, total, passed))
    print(f"\n{'Feature':<26}{'Tests':>6}{'Passed':>8}{'Failed':>8}")
    for title, total, passed in rows:
        print(f"{title:<26}{total:>6}{passed:>8}{total - passed:>8}")
    all_total, all_passed = sum(r[1] for r in rows), sum(r[2] for r in rows)
    print(f"{'TOTAL':<26}{all_total:>6}{all_passed:>8}{all_total - all_passed:>8}")
    print("RESULT:", "ALL TESTS PASSED" if all_total == all_passed else "FAILED")
