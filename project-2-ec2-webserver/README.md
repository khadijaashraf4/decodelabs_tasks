# Project 2: The Server Commander

## Scenario

A startup is launching a new dynamic application and needs a dedicated server environment with full control over the OS to install custom software and security patches.

## Mission

* Launch a Virtual Machine (EC2) using Ubuntu Server 24.04 LTS
* Connect securely via SSH
* Install a web server (Apache) via the command line
* Host a custom "Welcome to DecodeLabs" webpage

## Tools Used

* AWS EC2 (t3.micro, Ubuntu 24.04 LTS)
* SSH (OpenSSH client)
* Apache2

## Steps Taken

1. **Launched EC2 instance** — Ubuntu 24.04 LTS, t3.micro, new key pair, new security group.
2. **Configured security group** — SSH (22) restricted to My IP, HTTP (80) open to Anywhere (0.0.0.0/0).
3. **Connected via SSH**:

```bash
   ssh -i "decodeLabs-key.pem" ubuntu@<PUBLIC\_IP>
   ```

4. **Installed Apache**:

```bash
   sudo apt update \&\& sudo apt upgrade -y
   sudo apt install apache2 -y
   sudo systemctl status apache2
   ```

5. **Deployed custom webpage** — edited `/var/www/html/index.html` (see [`index.html`](./index.html) in this folder) via `sudo nano /var/www/html/index.html`.
6. **Verified** — opened `http://<PUBLIC\_IP>` in a browser and confirmed the custom page loads.

## Files in this folder

* `index.html` — the actual custom webpage deployed on the server
* `screenshots/` — evidence of each step (see table below)

## Screenshots

|#|File|Description|
|-|-|-|
|1|`screenshots/01-launch-instance.png`|EC2 launch config (instance name, AMI, instance type, key pair)|
|2|`screenshots/02-security-group.png`|Security group inbound rules (SSH + HTTP)|
|3|`screenshots/03-ssh-connection.png`|Terminal showing successful SSH connection|
|4|`screenshots/04-apache-install.png`|Terminal showing `apache2` install + `systemctl status` (active/running)|
|5|`screenshots/05-nano-edit.png`|The edited `index.html` in nano|
|6|`screenshots/06-live-page.png`|Browser showing the live page at the public IP|



