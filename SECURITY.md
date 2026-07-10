# Security Policy

## Project Status

Semantic RSVP Reader is an early-stage experimental project intended for local development, evaluation, and research.

It has not been reviewed, hardened, or certified for production deployment, exposure to untrusted networks, or handling sensitive information.

Security reports are nevertheless welcome. Responsible reports help prevent development defects from becoming established design assumptions.

## Supported Versions

Security fixes are applied only to the current `main` branch.

| Version                                   | Supported |
| ----------------------------------------- | --------: |
| Latest commit on `main`                   |       Yes |
| Older commits, forks, and archived builds |        No |
| Unreleased local modifications            |        No |

The project does not currently maintain long-term support branches or production release lines.

## Reporting a Vulnerability

Please do not publicly disclose a suspected vulnerability before the maintainers have had a reasonable opportunity to investigate it.

Use GitHub's private vulnerability reporting feature for this repository when available:

1. Open the repository's **Security** tab.
2. Select **Report a vulnerability**.
3. Submit the report privately.

If private vulnerability reporting is unavailable, open a public issue containing only a minimal notice that you have identified a possible security problem and need a private reporting channel.

Do not include exploit code, secrets, personal information, detailed reproduction instructions, or other information that would make the vulnerability easier to abuse in a public issue.

## Information to Include

A useful report should contain:

* a clear description of the suspected vulnerability;
* the affected commit, branch, file, or component;
* the environment in which it was reproduced;
* the steps required to reproduce it;
* the security impact;
* any conditions required for exploitation;
* proof-of-concept material, where appropriate;
* suggested mitigations, if known;
* whether the issue has been disclosed anywhere else.

Reports should distinguish between confirmed behavior and suspected impact.

Please remove or redact credentials, access tokens, private text, personal data, and unrelated system information.

## Relevant Security Areas

Reports are particularly useful when they concern:

* arbitrary code or command execution;
* path traversal or unintended file access;
* unsafe file upload or file parsing;
* cross-site scripting or HTML injection;
* request forgery;
* exposure of local files, user-provided text, logs, or reports;
* unsafe handling of configuration values or environment variables;
* dependency vulnerabilities with a demonstrated impact on this project;
* denial-of-service conditions caused by ordinary or crafted input;
* insecure default network binding or deployment behavior;
* unintended modification or corruption of evaluation artifacts;
* vulnerabilities in future parser or model-loading integrations.

This list is illustrative rather than exhaustive.

## Generally Out of Scope

The following are normally not treated as security vulnerabilities unless they create a concrete security impact:

* chunking-quality defects;
* incorrect phrase boundaries;
* timing or readability problems;
* visual layout defects;
* unsupported browsers or devices;
* performance differences within normal operating ranges;
* vulnerabilities that exist only in an obsolete dependency and cannot affect the project;
* reports produced solely by automated scanners without validation;
* theoretical concerns without a plausible attack path;
* denial-of-service scenarios requiring unrealistic local resource access;
* attacks requiring the user to deliberately execute already-untrusted code;
* issues in third-party services, forks, operating systems, browsers, or libraries that the project does not control.

Functional defects should be reported through the normal GitHub issue tracker.

## Response Process

After receiving a report, the maintainers will make a best-effort attempt to:

1. acknowledge the report;
2. determine whether the behavior is reproducible;
3. assess its scope and severity;
4. identify an appropriate mitigation;
5. prepare and test a correction;
6. coordinate disclosure when appropriate.

Because this is a volunteer-maintained experimental project, no fixed response or remediation time is guaranteed.

The reporter may be asked for additional technical information. Lack of reproducibility, insufficient detail, or absence of a concrete security impact may result in the report being closed without a code change.

## Disclosure

Please allow the maintainers reasonable time to investigate and correct a confirmed vulnerability before publishing technical details.

Once a correction is available, the maintainers may:

* publish a GitHub Security Advisory;
* reference the corrective commit;
* document affected versions or commits;
* credit the reporter, with permission;
* recommend mitigation or upgrade steps.

Reporter anonymity will be respected when requested, subject to the capabilities and requirements of the reporting platform.

## Research Guidelines

Good-faith security research is welcome when it:

* avoids accessing data that does not belong to the researcher;
* avoids disrupting services or other users;
* uses the minimum testing necessary to demonstrate the issue;
* does not rely on social engineering, physical intrusion, or credential theft;
* does not retain, alter, or publish sensitive information;
* follows applicable law;
* reports confirmed vulnerabilities responsibly.

This policy does not authorize testing against systems, deployments, accounts, or infrastructure operated by third parties.

## Secrets and Sensitive Data

Do not submit real credentials, access tokens, private keys, session data, personal text, or confidential documents as test fixtures, issue attachments, or repository content.

If a secret is accidentally committed:

1. revoke or rotate it immediately;
2. treat the secret as compromised even if the commit is later removed;
3. report the exposure privately;
4. remove it from the current tree and, where necessary, repository history.

Deleting a file or commit does not by itself invalidate an exposed credential.

## Dependencies

Dependency alerts and automated scanner results are useful signals, but they should be evaluated in the context of the project's actual execution paths.

A dependency report should explain:

* which dependency and version are affected;
* whether the vulnerable component is executed or reachable;
* how the project can trigger the vulnerable behavior;
* what mitigation or upgrade is available.

The maintainers may defer dependency changes that have no demonstrated impact, particularly when an upgrade would disrupt frozen evaluation or experimental baselines.

Confirmed exploitable vulnerabilities take precedence over ordinary feature work and evaluation freezes.

## Security Expectations for Deployment

Anyone deploying this project is responsible for securing their own environment.

At minimum:

* do not expose a development server directly to the public internet;
* use a maintained production server and reverse proxy where appropriate;
* restrict network access;
* validate deployment configuration;
* keep Python and project dependencies updated;
* avoid processing sensitive or untrusted content without additional review;
* protect logs, reports, uploaded text, and generated artifacts;
* run the application with the minimum required privileges;
* review future parser models and external assets before loading them.

The absence of a known vulnerability does not imply that a deployment is secure.
