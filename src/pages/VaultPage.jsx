import React from 'react'
import { Box, Link, Stack, Typography } from '@mui/material'
import { vaultFiles } from './vaultFiles'

const groups = [
  { key: 'ai', title: 'AI Practicals (BETCE15314)' },
  { key: 'se', title: 'SE Practicals (BETCE15322)' },
  { key: 'awd', title: 'AWD Practicals (BETCE15316)' },
]

const formatSize = (bytes) => bytes > 1024 * 1024 ? `${(bytes / 1024 / 1024).toFixed(1)} MB` : `${Math.max(1, Math.round(bytes / 1024))} KB`

export const VaultPage = () => {
  return (
    <Box sx={{ maxWidth: 900, mx: 'auto', p: 3 }}>
      <meta name="robots" content="noindex,nofollow" />
      {groups.map(({ key, title }) => (
        <Box key={key} sx={{ mb: 4 }}>
          <Typography variant="h6" sx={{ mb: 1 }}>{title}</Typography>
          <Stack spacing={0.5}>
            {vaultFiles[key].map((file) => (
              <Stack key={file.path} direction="row" justifyContent="space-between" columnGap={2}>
                <Link href={`/_v/${key}/${encodeURI(file.path)}`} target="_blank" rel="noopener noreferrer" underline="hover" sx={{ wordBreak: 'break-all' }}>
                  {file.path}
                </Link>
                <Typography variant="body2" color="text.secondary" sx={{ whiteSpace: 'nowrap' }}>{formatSize(file.size)}</Typography>
              </Stack>
            ))}
          </Stack>
        </Box>
      ))}
    </Box>
  )
}
