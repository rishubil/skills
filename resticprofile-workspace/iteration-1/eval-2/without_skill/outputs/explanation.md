# resticprofile Configuration Explanation

## Overview

This `profiles.toml` file defines three resticprofile profiles: `base`, `documents`, and `photos`.

## Profile Structure

### `base` Profile
The `base` profile holds all shared settings:
- **repository**: `/mnt/nas/backup` — the backup destination on the NAS
- **password-file**: `/root/.restic-password` — the file containing the repository encryption password
- **retention policy** (inside `[base.retention]`):
  - `keep-daily = 7` — keep the last 7 daily snapshots
  - `keep-weekly = 4` — keep the last 4 weekly snapshots
  - `keep-monthly = 12` — keep the last 12 monthly snapshots
  - `after-backup = true` — automatically run the forget/prune step after each backup

### `documents` Profile
- Inherits all settings from `base` via `inherit = "base"`
- Backs up `/srv/documents` as the source directory

### `photos` Profile
- Inherits all settings from `base` via `inherit = "base"`
- Backs up `/srv/photos` as the source directory
- Excludes `*.tmp` files from backups using the `exclude` option

## Inheritance

resticprofile's `inherit` key allows child profiles to reuse all settings from a parent profile without repetition. The `documents` and `photos` profiles each declare only what differs from `base` (source path, and exclusions for `photos`), while automatically inheriting the repository, password file, and retention policy.

## Usage Examples

```bash
# Run a backup for documents
resticprofile --name documents backup

# Run a backup for photos
resticprofile --name photos backup
```
