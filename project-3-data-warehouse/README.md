# Project 3: The Data Warehouse

## Scenario

An e-commerce company is struggling with Excel sheets to manage customer data. As their user base grows, they need a robust, scalable, and secure cloud database.

## Mission

* Provision a managed cloud database (Amazon RDS, MySQL)
* Create a table named `Interns` with columns: Name, Role, Email
* Insert dummy records to test data persistence
* (Bonus) Connect using a local SQL client / Python script over an SSH tunnel

## Tools Used

* AWS RDS (MySQL, db.t4g.micro, Free Tier)
* EC2 instance (from Project 2) used as a bastion host
* SSH local port forwarding (tunnel)
* MySQL Workbench
* Python + PyMySQL (bonus)

## Architecture

The RDS instance is **not publicly accessible** — it lives in a private subnet inside the same VPC as the EC2 instance. All access happens through an SSH tunnel forwarded through the EC2 bastion host, rather than exposing the database directly to the internet.

## Steps Taken

1. **Created RDS MySQL instance** — Standard/Full configuration, Public access = No, same VPC as EC2, connected via the "Connect to an EC2 compute resource" option (auto-wires the security groups).
2. **Verified security group rules** — RDS only accepts inbound MySQL (3306) traffic from the EC2 instance's security group, not from the public internet.
3. **Opened an SSH tunnel**:

```bash
   ssh -i "decodeLabs-key.pem" -L 3306:<RDS\\\_ENDPOINT>:3306 ubuntu@<EC2\\\_PUBLIC\\\_IP>
   ```

4. **Connected via MySQL Workbench** to `127.0.0.1:3306` (the tunnel forwards this to the real RDS endpoint).
5. **Created the table** — see [`schema.sql`](./schema.sql).
6. **Inserted dummy records** — see [`seed\\\_data.sql`](./seed_data.sql).
7. **Verified persistence** — see [`queries.sql`](./queries.sql).
8. **(Bonus)** Queried the same data with Python — see [`connect.py`](./connect.py).

## Files in this folder

* `schema.sql` — the `CREATE TABLE Interns (...)` statement
* `seed\\\_data.sql` — the `INSERT INTO Interns (...)` statements
* `queries.sql` — the verification `SELECT \\\* FROM Interns;` query
* `connect.py` — bonus Python/PyMySQL connection script (credentials removed — use environment variables, never commit real passwords)
* `screenshots/` — evidence of each step

## Screenshots

|#|File|Description|
|-|-|-|
|1|`screenshots/01-rds-instance.png`|RDS instance created (Available, MySQL, Public access = No)|
|2|`screenshots/02-security-group.png`|RDS security group inbound rule (port 3306, source = EC2 security group)|
|3|`screenshots/03-ssh-tunnel.png`|Terminal showing the SSH tunnel command running|
|4|`screenshots/04-workbench-connected.png`|MySQL Workbench connected via 127.0.0.1:3306|
|5|`screenshots/05-create-table.png`|CREATE TABLE query executed successfully|
|6|`screenshots/06-insert-records.png`|INSERT INTO query executed successfully|
|7|`screenshots/07-select-results.png`|SELECT \* FROM Interns; showing the returned rows|
|8|`screenshots/08-python-output.png`|(Bonus) Python script output|



