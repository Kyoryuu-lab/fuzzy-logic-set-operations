<h1>fuzzy-logic-set-operations</h1>
<p>Computational Intelligence: Fuzzy set theory, linguistic variables, membership functions, and set operations in Python</p>

<h2>Project description</h2>
<p>This project models approximate reasoning and fuzzy set theory on an empirical customer satisfaction domain $[0, 10]$ using NumPy and Matplotlib:</p>
<ol>
  <li>
    <dl>
      <dt><b>Linguistic Variable &amp; Terms:</b></dt>
      <dd>Defines continuous piecewise linear membership functions ($\mu(x) \in [0, 1]$).</dd>
      <dd>Partitions the domain into 5 linguistic categories: <i>Very Dissatisfied</i>, <i>Dissatisfied</i>, <i>Neutral</i>, <i>Satisfied</i>, and <i>Very Satisfied</i>.</dd>
    </dl>
  </li>
  <li>
    <dl>
      <dt><b>Standard Fuzzy Set Operations:</b></dt>
      <dd><b>Fuzzy Union (S-Norm):</b> Implements maximum-based aggregation $\mu_{A \cup B}(x) = \max(\mu_A(x), \mu_B(x))$.</dd>
      <dd><b>Fuzzy Intersection (T-Norm):</b> Implements minimum-based conjunction $\mu_{A \cap B}(x) = \min(\mu_A(x), \mu_B(x))$.</dd>
      <dd><b>Fuzzy Complement (Negation):</b> Implements standard involutive negation $\mu_{\neg A}(x) = 1 - \mu_A(x)$.</dd>
    </dl>
  </li>
  <li>Provides point-wise degree-of-membership evaluation via CLI (<code>--eval &lt;float&gt;</code>) and multi-curve visualization.</li>
</ol>

<h2>Project files</h2>
<table>
  <tr>
    <th colspan="2">fuzzy-logic-set-operations</th>
  </tr>
  <tr>
    <td>main.py</td>
    <td>Core model implementing membership functions, fuzzy operators, and plot generators</td>
  </tr>
  <tr>
    <td>README.md</td>
    <td>Project documentation and mathematical specification</td>
  </tr>
  <tr>
    <td>.gitignore</td>
    <td>Exclusion rules for bytecode, virtual environments, and generated plots</td>
  </tr>
</table>

<h2>Mathematical Formulation of Membership Functions</h2>
<table>
  <tr>
    <th>Linguistic Term</th>
    <th>Analytical Definition $\mu(x)$</th>
    <th>Core Support Range</th>
  </tr>
  <tr>
    <td><b>Very Dissatisfied</b></td>
    <td>$\max(1 - x / 3, 0)$</td>
    <td>$[0, 3]$</td>
  </tr>
  <tr>
    <td><b>Dissatisfied</b></td>
    <td>$\max(\min((x - 2) / 2, (6 - x) / 2), 0)$</td>
    <td>$[2, 6]$ (Center at $x = 4$)</td>
  </tr>
  <tr>
    <td><b>Neutral</b></td>
    <td>$\max(\min(x - 4, 6 - x), 0)$</td>
    <td>$[4, 6]$ (Center at $x = 5$)</td>
  </tr>
  <tr>
    <td><b>Satisfied</b></td>
    <td>$\max(\min((x - 6) / 2, (9 - x) / 2), 0)$</td>
    <td>$[6, 9]$ (Center at $x = 7.5$)</td>
  </tr>
  <tr>
    <td><b>Very Satisfied</b></td>
    <td>$\max((x - 7) / 3, 0)$</td>
    <td>$[7, 10]$</td>
  </tr>
</table>

<h2>Installation and launch</h2>
<ol>
  <b>
    <li>
      <dl>
        <dt>Clone repository</dt>
        <dd>
          <code>git clone https://github.com/Kyoryuu-lab/fuzzy-logic-set-operations.git</code>
        </dd>
        <dd>
          <code>cd fuzzy-logic-set-operations</code>
        </dd>
      </dl>
    </li>
  </b>
  <b>
    <li>
      <dl>
        <dt>Install dependencies</dt>
        <dd>
          <code>pip install numpy matplotlib</code>
        </dd>
      </dl>
    </li>
  </b>
  <b>
    <li>
      <dl>
        <dt>Run visualizer and point evaluation</dt>
        <dd>Display plot and evaluate $x = 4.5$: <code>python main.py --eval 4.5</code></dd>
        <dd>Save plot directly as PNG image: <code>python main.py --save</code></dd>
      </dl>
    </li>
  </b>
</ol>

<h2>Example of console output (python main.py --eval 4.5)</h2>
<samp>
  <p>
    ============================================================<br />
    &nbsp;&nbsp;FUZZY MEMBERSHIP EVALUATION FOR x = 4.50<br />
    ============================================================<br />
    &nbsp;&nbsp;Very Dissatisfied&nbsp;&nbsp;&nbsp;: mu = 0.0000<br />
    &nbsp;&nbsp;Dissatisfied&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;: mu = 0.7500<br />
    &nbsp;&nbsp;Neutral&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;: mu = 0.5000<br />
    &nbsp;&nbsp;Satisfied&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;: mu = 0.0000<br />
    &nbsp;&nbsp;Very Satisfied&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;: mu = 0.0000<br />
    ============================================================<br />
  </p>