# This code is part of QSteed.
#
# (C) Copyright 2024 Beijing Academy of Quantum Information Sciences
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from qsteed.compiler.compiler import Compiler
from qsteed.utils.random_circuit import RandomCircuit
from quafu import QuantumCircuit
from quafu.elements.parameters import Parameter


rc = RandomCircuit(num_qubit=5, depth=6, gates_list=['rxx', 'cx', 'h', 'x', 'y', 'z'])
qc = rc.random_circuit()

pq = QuantumCircuit(5)
theta = [Parameter("theta_%d" % i, 0.1) for i in range(10)]
theta[4].value = 3.3
pq.rx(1, 0.8)
pq.rx(1, theta[2] * theta[4] * theta[3])
pq.rx(1, 2 * theta[4])
pq.ry(2, theta[5] + 0.9)
pq.rx(3, theta[6])
pq.rx(4, theta[7])
pq.rxx(0, 3, theta[0])
pq.rzz(2, 3, theta[8])
pq.rzz(0, 2, theta[4])
pq.rx(0, theta[9])
pq.rx(0, 3.5)
pq.cx(3, 4)
pq.ry(2, theta[1].sin() - 4. * theta[0] + theta[2] * theta[0] + 2.5)
pq.rx(2, theta[1] - 4. * theta[0] + theta[2] * theta[0])
pq.measure([0, 1, 2, 3, 4], [0, 1, 2, 3, 4])

qasm = """
OPENQASM 2.0;
include "qelib1.inc";
qreg q[10];
creg meas[4];
h q[3];
cx q[3],q[5];
cx q[5],q[8];
cx q[8],q[2];
barrier q[3],q[5],q[8],q[2];
measure q[3] -> meas[0];
measure q[5] -> meas[1];
measure q[8] -> meas[2];
measure q[2] -> meas[3];
"""

unqasm = """
OPENQASM 2.0;
include "qelib1.inc";
qreg q[10];
creg meas[4];
h q[2];
cx q[2],q[3];
cx q[3],q[4];
cx q[4],q[5];
barrier q[2],q[3],q[4],q[5];
measure q[2] -> meas[0];
measure q[3] -> meas[1];
measure q[4] -> meas[2];
measure q[5] -> meas[3];
"""

unqasmpara = 'OPENQASM 2.0;\ninclude "qelib1.inc";\nqreg q[130];\ncreg meas[5];\ntheta_5 = 0.1;\ntheta_6 = 0.1;\ntheta_7 = 0.1;\ntheta_2 = 0.1;\ntheta_4 = 3.3;\ntheta_3 = 0.1;\ntheta_0 = 0.1;\ntheta_8 = 0.1;\ntheta_1 = 0.1;\ntheta_9 = 0.1;\nry((theta_5 + 0.9)) q[88];\nrx(theta_6) q[87];\nrx(theta_7) q[86];\nrx((((theta_2 * theta_4 * theta_3 + 0.8) + 0) + theta_4 * 2)) q[90];\ncx q[89],q[88];\nh q[87];\ncx q[88],q[89];\ncx q[89],q[88];\nh q[88];\ncx q[88],q[87];\nrz(theta_0) q[87];\ncx q[88],q[87];\nh q[88];\nh q[87];\ncx q[88],q[89];\ncx q[89],q[88];\ncx q[88],q[89];\ncx q[88],q[87];\nrz(theta_8) q[87];\ncx q[88],q[87];\ncx q[89],q[88];\ncx q[87],q[86];\nrz(theta_4) q[88];\ncx q[89],q[88];\nry((((sin(theta_1) - theta_0 * 4.0) + theta_2 * theta_0) + 2.5)) q[88];\nrx(((theta_9 + 0) + 3.5)) q[89];\nrx(((theta_1 - theta_0 * 4.0) + theta_2 * theta_0)) q[88];\nbarrier q[86],q[87],q[88],q[89],q[90];\nmeasure q[89] -> meas[0];\nmeasure q[90] -> meas[1];\nmeasure q[88] -> meas[2];\nmeasure q[87] -> meas[3];\nmeasure q[86] -> meas[4];\n'

# qc = 'OPENQASM 2.0;\ninclude "qelib1.inc";\nqreg q[6];\ncreg meas[6];\nrxx(4.0026966352019935) q[5],q[1];\nrxx(4.945686274927422) q[0],q[2];\nrxx(0.02383128902615615) q[5],q[1];\nrxx(2.583395631862997) q[2],q[5];\nid q[3];\nid q[4];\nmeasure q[0] -> meas[0];\nmeasure q[1] -> meas[1];\nmeasure q[2] -> meas[2];\nmeasure q[3] -> meas[3];\nmeasure q[4] -> meas[4];\nmeasure q[5] -> meas[5];\n'

compiler = Compiler(unqasmpara, qpu_name='example', optimization_level=1, transpile=True)
compiled_openqasm, final_q2c, compiled_circuit_information = compiler.compile()

from quafu import QuantumCircuit
import matplotlib.pyplot as plt
qc = QuantumCircuit(130)
qc.from_openqasm(compiled_openqasm)
qc.draw_circuit()
# qc.plot_circuit()
# plt.show()

