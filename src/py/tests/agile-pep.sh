#!/bin/bash
export owner_token="qDY2n12mDjWLqTDK2aRLJBY9iI4UkbsYOs1EXHDWMHuJuQ76Erlvoyz3wXEM0Dqp"
export doctor_token="L9GV2k239Qz2SwmW9soptoJa58V4UJyi94qe2WDXxihQr3eFKoWjlbbb1TuhDbOA"
export paramed_token="goi0FmqH3DQ9y2PDtJ4qNiWJ7rOVdUPe6lyY5qOBfb1C7ymgJmqxUgGm0SRXGfZQ"

echo "# STARTING POLICY EVALUATION TESTS"
echo
./tests/policy-tests/pos_eval_cumul_read.sh
# ./tests/policy-tests/pos_eval_cumul_write.sh
./tests/policy-tests/neg_eval_cumul_read.sh
./tests/policy-tests/neg_eval_cumul_write.sh
echo
echo "# Success for agile-pep.py!"
echo
