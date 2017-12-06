#!/bin/bash
export owner_token="1M65kYk6mzATHl7fghKiuypnsCZH7zS4u0taQzuA2cqlrSh8pqIf6ZyoAKJFA4Tv"
export doctor_token="cZjIfZxd4OGU3G44Nca3HOYZDRrlv6Kds8s8BbSdPStu8uSWNJ2mnFBQ1cgrr8Ca"
export paramed_token="lB9113eXEFWq3yHaQ1ftrc3xzoXBQGozKzpgeo6d9abYNhEVfDuvpkK3IXPLra2e"

echo "# STARTING POLICY EVALUATION TESTS"
echo
./tests/policy-tests/policy_db.sh
# ./tests/policy-tests/policy_db-tables.sh
# ./tests/policy-tests/policy_db-columns.sh
echo
echo "# Success for agile-pep.py!"
echo
