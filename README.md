# yum-plugin-monit

yum plugin to temporarily deactivate monit during package installs / updates / removals.

# Installation

```bash
make install
```

# Uninstallation

```bash
make uninstall
```

# Build RPM

```bash
rpmbuild --undefine=_disable_source_fetch -ba yum-plugin-monit.spec
```

# How It Works

The plugin uses two hooks:
  * `pretrans_hook` which fires right before the transaction; this hook function stops monit (using `systemctl`)
  * `posttrans_hook` which fires after the transaction is completed; this function starts monit (using `systemctl`)


# Why

Consider the following configuration:

```
check file sshd_bin with path /usr/sbin/sshd
  if failed checksum       then unmonitor
  if failed permission 755 then unmonitor
  if failed uid root       then unmonitor
  if failed gid root       then unmonitor
```

Everything works untils you update `openssh-server` package: when `/usr/sbin/sshd` is replaced with a new version,
this triggers `if failed checksum then unmonitor` rule, and ssh is no longer monitored.

With this plugin, monit is stoped before the transaction is run and started again after the transaction is completed.
Upon start, monit recaluclates all checksums and therefore `sshd` is not get unmonitored.
