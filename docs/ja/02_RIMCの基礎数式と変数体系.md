

# 2 RIMCの基礎数式と変数体系

**Chapter 2 — The Foundational Equations of RIMC**
_Coupled Dynamics Between Technological Recursiveness and Market Value_

---

## 2.1 仮説の枠組み

RIMCは、**技術再帰率（R）** と **経済的価値（V）** が相互依存的に変化する  
**動的連成系（Dynamic Coupled System）** として定義される。

中心的前提は、

> **「技術が資本を生み、資本が技術を加速させる」**

という再帰構造にある。

ここでの技術再帰率 $\mathbf{R}(t)$ は、単一のスカラーではなく、
研究開発・データ資産・組織学習・ネットワークなど、複数の要素の**相互作用**として表される多次元ベクトルである。

分析便宜上、価値生成に寄与する主要成分を **集約関数 $h(\mathbf{R})$** によりスカラー化して扱う。
すなわち、状態変数として扱うスカラーは以下で定義される：

$$
r(t) = h(\hat{\mathbf{R}}(t)) \quad (\ge 0)
$$

---

## 2.2 基本連立方程式(RV方程式)

第1章で提示した最小連立式は、RIMCの基本的な再帰構造を抽象的に表したものである。  

本章ではそれを現実的な観測構造を導入し、遅延・減衰・非線形項を明示的に組み込むことで、  
より一般化された操作的定義として再構築する。

市場は技術を直接観測できず、開示・報道などの外部シグナルを通じて推定する。
この観測構造の形式定義は第3章（3.2）に詳述するが、ここでは概要として
$\hat{\mathbf{R}}(t)$ が実際の $\mathbf{R}(t)$ の遅延同化結果であることのみ確認しておく。

RIMCの双ループを以下の形で定義する：

$$
\boxed{
\begin{cases}
\dfrac{dV}{dt} = L(t) \cdot A(t) \cdot [r(t-\tau)]^{\beta(t)} - \kappa_V(t) \cdot V(t)^{\mu(t)} \\
\dfrac{dr}{dt} = \gamma(t) \cdot V(t)^{\delta(t)} - \kappa_R(t) \cdot r(t)^{\nu(t)}
\end{cases}
}
$$
なお、ここでの $r(t)$ は便宜的に「市場推定を含む代表的再帰率」として扱う。  
技術の実体的進化（$r_{\text{real}}$）と市場が観測する再帰率（$r_{\text{market}}$）の
非同期構造は第3章にて数理的に分離する。

> **符号と範囲の前提**：
> $L(t),A(t),\gamma(t) > 0$, $\beta(t),\delta(t) > 0$,
> $\kappa_V(t),\kappa_R(t) \ge 0$, $\mu(t),\nu(t) \ge 1$, $\tau \ge 0$

| 記号                        | 名称           | 概要                     |
| ------------------------- | ------------ | ---------------------- |
| $V(t)$                    | 経済的価値        | 市場で観測される価値（時価総額・収益など）  |
| $r(t)$                    | 技術再帰率（スカラー化） | 技術・知識・情報構造の自己改良力を集約した値 |
| $\hat{\mathbf{R}}(t)$     | 観測推定R        | 外部シグナルから市場が同化したR       |
| $L(t)$                    | 社会受容速度       | 制度・文化的慣性を含む学習速度        |
| $A(t)$                    | 資本集中率        | 資本・注意・リソースの集中度         |
| $\beta(t)$                | 技術の非線形性      | **superlinear** な増幅度   |
| $\gamma(t),\delta(t)$     | 価値→技術の感応     | 経済成果が次の技術投資を促す強度       |
| $\kappa_V(t),\kappa_R(t)$ | 減衰項          | 飽和・競争・規制などのブレーキ        |
| $\tau$                    | 観測遅延         | 技術→価値反映までの時間差          |

> **備考**：
> $\beta(t),\delta(t)>1$ かつ $\kappa_V(t),\kappa_R(t)\to0$ のとき、
> $L(t),A(t),\gamma(t)$ が大きいと系の内部正帰還が強すぎる場合、自己励起的挙動が発生し得る。  
> RIMCでは、安定性を担保するために $\kappa_V(t),\kappa_R(t)>0$ を前提とし、  
> 定常上限を設定することで数値的安定を維持する。

---

### 2.2.1 モデルの成立条件と正値不変性（Assumptions）

**仮定A（R–V連成系の良置性）**

**前提：**

* $h \in C^1$ で局所Lipschitz、成長は高々多項式。
* $L(t),A(t),\gamma(t)$ は有界・区分的連続。
* $\kappa_V(t),\kappa_R(t)>0,\ \mu(t),\nu(t)\ge1$。
* 初期履歴 $V(\cdot),r(\cdot):[-\tau,0]\to[0,\infty)$。

**結論：**

$$
\begin{cases}
\dfrac{dV}{dt} = L(t)A(t)[r(t-\tau)]^{\beta(t)} - \kappa_V(t)V(t)^{\mu(t)} \\
\dfrac{dr}{dt} = \gamma(t)V(t)^{\delta(t)} - \kappa_R(t)r(t)^{\nu(t)}
\end{cases}
$$

は、少なくとも局所時間内で一意解を持ち、
さらに $V(t),r(t)\ge0$ が保たれる。

境界でのベクトル場は $V=0 \Rightarrow \dot V \ge 0$, $r=0 \Rightarrow \dot r \ge 0$ を満たすため、
**第1象限は正値不変** である。

---

### 2.2.2 オペレーショナル定義：時変推定パラメータ

RIMCの諸パラメータ
$L(t),A(t),\gamma(t),\delta(t),\kappa_V(t),\kappa_R(t),\beta(t),\mu(t),\nu(t),\tau$ は、
固定定数ではなく、 **データ駆動的に再推定される時変パラメータ群** として扱う。

これらは、マクロ的・制度的・情報的系列 $Z_t$ からの写像であり、
各時点 $t$ ごとに再評価される動的パラメータである：

$$
\begin{aligned}
L(t) &= \mathcal{L}(Z_t;\theta_L), \quad
A(t) = \mathcal{A}(Z_t;\theta_A), \\\
\gamma(t) &= \Gamma(Z_t;\theta_\gamma), \quad
\beta(t) = \mathcal{B}(Z_t;\theta_\beta), \quad
\delta(t) = \Delta(Z_t;\theta_\delta), \\\
\kappa_V(t) &= \mathcal{K}_V(Z_t;\theta_{K_V}), \quad
\kappa_R(t) = \mathcal{K}_R(Z_t;\theta_{K_R}), \\\
\mu(t) &= M_V(Z_t;\theta_\mu), \quad
\nu(t) = N_R(Z_t;\theta_\nu)
\end{aligned}
$$

---

### 2.2.3 観測構造とスカラー化

観測層では、内部構造 $\mathbf{R}(t)$ が外部化オペレータ $\mathcal{O}$ を通じて
象徴層 $S(t)$（Symbolic layer）として可視化され、
それを市場が同化オペレータ $\mathcal{I}$ により解釈する：

$$
S(t)
= \mathcal{O}\big(\mathbf{R}(t-\tau_{\mathcal{O}})\big) + \eta(t),
\qquad
\hat{\mathbf{R}}(t)
= \mathcal{I}\big(S(t-\tau_{\mathcal{I}})\big)
$$

ここで：

* $\tau_{\mathcal{O}}, \tau_{\mathcal{I}}$：外部化・同化の遅延
* $\eta(t)$：観測ノイズ
* $S(t)$：技術活動が社会的プロセスを通じて **情報的表現** へ変換された集合

これにより、市場が認識する再帰率は次のように定義される：

$$
r_{\text{market}}(t) = h(\hat{\mathbf{R}}(t))
$$

一方、内部で生成される真の再帰率は：

$$
r_{\text{real}}(t) = h(\mathbf{R}(t))
$$

であり、両者の差 $\varepsilon_R(t)=r_{\text{real}}(t)-r_{\text{market}}(t)$
が後章で扱う **観測差** を構成する。

本節では観測層の基本形を定義したが、  
その実際の情報流（外部化と同化の遅延構造）は次章で詳述する。

---

### 2.2.4 RIMC構造における S(t) の位置

RIMCの情報流れは、概念的に次のように整理できる：

$$
\mathbf{R}(t)
\xrightarrow[\text{開示・報道}]{\mathcal{O}}
S(t)
\xrightarrow[\text{市場解釈}]{\mathcal{I}}
\hat{\mathbf{R}}(t)
\xrightarrow[\text{スカラー化}]{h}
r_{\text{market}}(t)
$$

したがって $S(t)$ は **「外部化された情報状態（Symbolic layer）」** にあたる。  
すなわち、

> 企業内部の再帰構造が、報道・決算・SNS・分析記事などの形で  
> **外部に表出した情報的出力** を指す。

この層は、RIMCの三層構造（ **内部層・観測層・市場層** ）の中間に位置する：

| 層 | 主体 | 変数 | プロセス |
|:--|:--|:--|:--|
| 内部層 | 企業・技術 | $\mathbf{R}(t)$ | 技術・知識の生成 |
| **観測層** | 報道・分析 | **$S(t)$** | 外部化（$\mathcal{O}$）＋ノイズ |
| 市場層 | 投資家 | $\hat{\mathbf{R}}(t)$ | 同化・再構成（$\mathcal{I}$） |

---
### 2.2.5 時変推定関数の統合表現

観測遅延を含む形で、再帰率の時系列投影は次のように一般化できる：

$$
r_{\text{market}}(t-\tau)
= \mathcal{H}\!\left(
\Phi\big(\hat{\mathbf{R}}(t-\tau)\big)\;
\theta_H
\right)
$$

ここで $\Phi(\cdot)$ は領域固有の特徴抽出関数
（例：研究開発費、データ資産指標、人的資本、規制イベントなど）であり、
各 $\mathcal{F}\in{\mathcal{L},\mathcal{A},\Gamma,\mathcal{B},\Delta,\mathcal{K}_V,\mathcal{K}_R,\mathcal{H}}$ は
前処理・学習パイプラインとして構築され、
時点 $t$ ごとに再推定した係数を主方程式へ投入する。

---
### 2.2.6 パラメータの代理観測性（Proxy Assumption）

RIMCにおける各パラメータ
$L(t), A(t), \gamma(t), \beta(t), \delta(t), \kappa_V(t), \kappa_R(t)$ 等は、
**直接観測できる実体ではなく、外生系列 $Z_t$ に依存して推定される代理変数（proxy variables）** である。

すなわち、RIMCの主方程式に含まれる各項は以下のように定義される：

$$
\theta_i(t) = \mathcal{F}_i(Z_t; \theta_i)
\quad \text{for} \quad
\theta_i \in {L,A,\gamma,\beta,\delta,\kappa_V,\kappa_R}
$$

ここで $\mathcal{F}_i$ は観測系列 $Z_t$（例：研究開発費、政策指標、報道頻度、産業構造データ等）を
入力とする推定関数であり、実務上は統計・機械学習モデルとして構築される。

この構造により、RIMCは
**「直接観測不能な技術再帰構造（内生層）」と
「観測可能な市場系列（外生層）」** を
データ駆動的に接続する枠組みとして機能する。

---

## 2.3 式(1)：技術→価値の再帰伝播

$$
\dfrac{dV}{dt} = L(t) \cdot A(t) \cdot [r(t-\tau)]^{\beta(t)} - \kappa_V(t) \cdot V(t)^{\mu(t)}
$$

この式は、**技術再帰率の上昇がどのように経済的価値を生むか**を示す。

* $r(t-\tau)$ により、市場が**遅延した情報**をもとに価値を形成する構造が表現される。
* $\beta(t)>1$ のとき、$r$ の微小な変化が指数的に価値を押し上げる **超線形増幅（superlinear amplification）** が生じる。
* $\kappa_V(t) \cdot V(t)^{\mu(t)}$ は、規模の飽和・競争の激化・社会的抵抗などを表す **減衰項**。

---

## 2.4 式(2)：価値→技術再帰へのフィードバック

$$
\dfrac{dr}{dt} = \gamma(t) \cdot V(t)^{\delta(t)} - \kappa_R(t) \cdot r(t)^{\nu(t)}
$$

経済的価値 $V(t)$ の拡大は、研究開発・人材投資・設備更新・データ獲得などを通じて
**技術再帰率の成長**を促す。

* $\gamma(t)$ は **資本が技術をどの程度加速できるか** を表す比例因子。
* $\delta(t)$ は経済的成功が技術成長にどの程度効くかの **感応度**。
* 減衰項 $\kappa_R(t) \cdot r(t)^{\nu(t)}$ は **リソース制約・飽和・制度摩擦** によるブレーキを表す。

この式は、経済成果が次の技術成長を誘発する **自己増幅的な正帰還構造** を形式化したものであり、
RIMCの「資本が技術を増幅する」側の再帰ループを担う。

---

## 2.5 無次元化と次元整合

時間基準 $T_0$、価値基準 $V_0$、再帰基準 $R_0$ を用い、
 $\tilde t=t/T_0,\ \tilde V=V/V_0,\ \tilde r=r/R_0$ と定義する。

すると、
$$
\frac{d\tilde V}{d\tilde t}
=\tilde L(\tilde t)\tilde A(\tilde t)\tilde r^\beta
-\tilde\kappa_V\,\tilde V^\mu
$$

となり、$\tilde L\tilde A$ は無次元量となる。
以降、全式は無次元変数で表す。

---

## 2.6 R–V連成系の意味：技術資本エンジン

RV方程式は、**技術が価値を生み、価値が技術を加速する**  
という非線形ループを最小構成で表す。  

しかし、市場は常に遅延 $\tau$ を伴って技術を観測しており、  
$\mathbf{R}_{\text{real}}(t)$（実際の技術）と $\mathbf{R}_{\text{market}}(t) \equiv \hat{\mathbf{R}}(t)$ の間には **非同調** が生じる。  

技術と市場推定の差を、**観測乖離（observation gap）** として次のように定義する：

$$
\varepsilon_R(t) = r_{\text{real}}(t) - r_{\text{market}}(t)

$$

この $\varepsilon_R$ が正のとき、  
$\varepsilon_R>0$ の場合、市場は技術進化を過小評価しており、  
情報遅延の修正過程を通じて $V(t)$ が後追い的に上昇する。
すなわちこの「観測差」こそが、RIMCにおける**超過リターン $\alpha$** の根源である。  

>RIMCでは、$\alpha$ は確率的残差ではなく、  
> 「技術生成速度」と「市場学習速度」の非同期性から導かれる  
> **情報的ドリフト（informational drift）** として再定義される。

この連成系は、**技術資本エンジン** として機能し、  
社会全体のイノベーション周期、産業の再編、資本の集中を説明する中核構造となる。

この乖離 $\varepsilon_R(t)$ の時間積分が、観測上の$\alpha$として定義される（第3章にて展開）。
すなわち、$\alpha$とは静的な誤差ではなく、時間を通じて累積される観測差の**履歴依存的量**である。

---

## 2.7 観測構造のズレから生成構造へ

ここまでに示したR–V連成系は、 **技術（$R$）が価値（$V$）を生み、価値が技術を加速する** という  
仮説上の閉じた再帰構造を記述している。

しかし現実の市場と技術の進化過程は、**完全には同調していない** 。  
市場が観測するのは、常に **過去の$R$** であり、  
しかもその観測過程には **情報伝達の遅延（$τ$）** や **同化誤差（$ε_R$）** が内在する。

すなわち市場は、

> 市場は「技術変化を後追い的に観測するシステム」であり、  
> 「技術を生成するシステム」ではない。

この **観測と生成の時間的非同期性** が、  
RIMCにおける「構造的リターン（$\alpha$）」の生成要因をなす。

次章では、この非同期がどのように **再帰ギャップ** として現れ、  
それが時間的に積分されて **超過リターン（$\alpha$）** を形成するかを定式化する。
