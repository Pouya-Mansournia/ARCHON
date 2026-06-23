# Linux Fundamentals

## Goal

Every server-side system you'll ever architect ultimately runs on Linux (directly, in a container, or inside a VM). A shaky mental model of Linux causes mysterious-looking production problems that are actually well-understood OS behavior.

## Processes & Resource Management

- A process has a PID, a parent PID, and inherits environment/file descriptors from its parent at fork time.
- `systemd` is the standard init system on modern distros (Ubuntu, RHEL, Debian, Amazon Linux 2+). Services are defined as unit files (`/etc/systemd/system/*.service`); use `systemctl start/stop/restart/status/enable` and `journalctl -u <service>` for logs.
- Resource limits matter in production: `ulimit` (file descriptors, processes), cgroups (CPU/memory limits — the same mechanism Docker/Kubernetes use under the hood). A process silently dying under load is very often hitting an open-file-descriptor or memory cgroup limit, not an application bug.
- OOM killer: Linux will kill processes when the system runs out of memory, prioritizing by an `oom_score`. A container restarting with no application-level error in the logs is the signature of an OOM kill — check `dmesg` or `journalctl -k`.

## File Permissions

- `rwx` for owner/group/other, represented as a 3-digit octal (e.g., `755` = owner rwx, group r-x, other r-x).
- `chmod`, `chown`, `chgrp` are the core tools. Setuid/setgid/sticky bits exist but are rarely needed in modern application architecture — if you find yourself reaching for them, ask whether a different process boundary or container would solve the actual problem more cleanly.
- The most common production permission bug: a deploy process running as a different user than the application process, leaving files the app can't read/write (log files, upload directories, socket files).

## Filesystems

- `ext4` is the safe, boring default for most Linux servers. `xfs` is common on RHEL-derived systems and performs well for large files. Both are fine choices — don't spend decision-making time here unless you have a specific, measured I/O bottleneck.
- Inodes are a real, finite resource separate from disk space — "no space left on device" with disk space free is almost always an inode exhaustion problem, common when an application creates huge numbers of small files (e.g., unbounded log file rotation, session files on disk).
- Mount points and `/etc/fstab` matter for anything attaching network storage (NFS, EBS volumes) — know whether a mount is `noatime` (better write performance, standard for most workloads) and what happens to the application if the mount becomes unavailable mid-operation.

## Package Management

- Debian/Ubuntu: `apt`. RHEL/Amazon Linux: `yum`/`dnf`. Know which your base image uses — this determines available packages and security patch cadence.
- Pin versions in production (`apt-get install nginx=1.24.0-*`), don't float on `latest` for anything that affects application behavior — silent minor-version upgrades are a real, recurring source of "it worked yesterday" incidents.

## Shell Tooling Every Engineer Should Be Fluent In

- `grep`, `awk`, `sed` for text processing during incident response — being able to grep a log file under pressure is a faster diagnostic path than waiting for a dashboard to load.
- `lsof` (list open files — including sockets) to answer "what process is holding port 8080" or "what's using this file."
- `strace`/`ltrace` for deep debugging when a process is behaving inexplicably (rare need, but invaluable when you hit it).
- `htop`/`top`, `iostat`, `vmstat`, `df -h`, `free -h` for live resource diagnosis during an incident — these should be muscle memory, not something you look up at 3am.

## Decision Rule

For any "what Linux distro / base image should we use" question: default to the most common, longest-support-window LTS distro your cloud provider and team already have the most operational familiarity with (commonly Ubuntu LTS or Amazon Linux 2023 on AWS). Exotic distro choices need a specific, named justification (e.g., a hard real-time kernel requirement points toward a different OS entirely — see `skills/11_Robotics/reference/embedded-realtime-control.md`).

## Common Mistakes

- Treating container restarts as application bugs without first checking for OOM kills.
- Running production services as `root` instead of a dedicated least-privilege user.
- Letting log files grow unbounded without `logrotate` or equivalent, eventually filling the disk and taking down the whole host.
- Assuming filesystem writes are durable immediately — without an `fsync`, data can still be lost on power failure even after a successful write() call returns.
