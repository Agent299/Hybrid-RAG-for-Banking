# Runbooks

## Check API liveness

Start the API using the root README. From the repository root, run `scripts/smoke.sh`. Set `API_BASE_URL` for an alternate local address. A successful probe prints the liveness JSON. For a failed probe, verify the process, address and listening port.

## Configure delivery controls

Once CI has reported its `merge-gate` check, a repository administrator can require it on protected main and configure independent review. Activate CODEOWNERS entries after identifying the approved owners. Keep staging and production disabled until their adapters and environments are configured. Production requires environment approval and signed artifact verification.
