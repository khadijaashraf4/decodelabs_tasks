# DecodeLabs — Cloud Computing Internship (Batch 2026)

This repository documents my hands-on projects from the **Cloud Computing (AWS/Azure) Internship** at DecodeLabs. Each project focuses on a core cloud computing concept, implemented and deployed using real AWS or Azure services.

## Projects

### Project 1 — The Global Launch
Deployed a static portfolio website using **Azure Blob Storage's Static Website Hosting** feature — no traditional server or VM involved.

**Tools used:** Azure Blob Storage, Static Website Hosting, HTML/CSS

**Live site:** https://khadijaportfolio2026v2.z29.web.core.windows.net/

**What I learned:**
- Object storage vs. traditional servers (IaaS)
- Static website hosting configuration
- Public HTTPS endpoints without manual SSL setup
- Cloud region/zone allowlists and troubleshooting deployment errors

---

### Project 2 — The Server Commander
Provisioned a dedicated Linux virtual server on **AWS EC2**, connected to it securely over SSH, and manually installed and configured a web server from the command line to host a custom page.

**Tools used:** AWS EC2 (Ubuntu 24.04 LTS, t3.micro), SSH, Apache2

**Project folder:** [`project-2-ec2-webserver/`](./project-2-ec2-webserver)

**What I learned:**
- The difference between IaaS (full OS control) and managed/static hosting
- Configuring security groups as a stateful firewall (SSH restricted to my IP, HTTP open to the public)
- Generating and securing an SSH key pair, including fixing Windows file-permission issues (`icacls`)
- Installing and managing a web server (`apt`, `systemctl`) directly via the command line
- Diagnosing real deployment issues: port conflicts (`nginx` already bound to port 80), dynamic IP addresses breaking security group rules, and SSH connection troubleshooting

---

### Project 3 — The Data Warehouse
Provisioned a managed, **privately networked** MySQL database on **AWS RDS** to replace a spreadsheet-based data workflow, and accessed it securely through an SSH tunnel rather than exposing it to the public internet.

**Tools used:** AWS RDS (MySQL), EC2 (as a bastion host), SSH port forwarding, MySQL Workbench, Python + PyMySQL (bonus)

**Project folder:** [`project-3-data-warehouse/`](./project-3-data-warehouse)

**What I learned:**
- Why a public database is a security liability, and how to isolate one in a private subnet
- Using an existing EC2 instance as a bastion host to safely reach a private resource
- Setting up local SSH port forwarding (tunneling) to connect a GUI SQL client to a database with no public endpoint
- Enforcing data integrity at the schema level with `PRIMARY KEY`, `UNIQUE`, and `NOT NULL` constraints
- Verifying data persistence end-to-end, from `INSERT` through to a `SELECT` proving the record survived
- Connecting programmatically with Python (`pymysql`) as an alternative to a GUI client

---

### Project 4 — The Serverless Logic
Deployed a lightweight "Cost Calculator" API as an **AWS Lambda** function — code that runs only when triggered and costs nothing while idle, instead of paying for an always-on server.

**Tools used:** AWS Lambda (Python 3.13), auto-generated IAM Execution Role, Amazon CloudWatch Logs

**Project folder:** [`project-4-serverless-logic/`](./project-4-serverless-logic)

**What I learned:**
- The core trade-off between traditional servers (EC2) and serverless/FaaS compute (pay-per-execution vs. pay-per-hour)
- Writing a Lambda handler function that parses an event payload and returns a JSON-serializable response
- The Principle of Least Privilege: Lambda functions have zero permissions by default until an IAM Execution Role grants them specific access
- Simulating real-world API traffic using mock test events in the console, without building a front end
- Reading CloudWatch logs to verify exact execution duration and billed duration, proving the millisecond-level cost efficiency of serverless compute

---

*More projects to be added as the internship progresses.*
