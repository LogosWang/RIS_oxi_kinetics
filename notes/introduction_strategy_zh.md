研究对象是 **304SS，以 Fe–Cr–Ni–Si 表示**。Introduction 的主线是：**RIS 改变晶界成分，选择性氧化和 SiO₂ 溶解改变氧化物组成与自由体积，由此改变同一个有效氧扩散系数 D_eff，进而影响氧化前沿的剂量和时间依赖。**

在本模型中，氧化层的“保护性”就是其限制氧传输的能力。氧化物 Cr 含量增加使 D_eff 降低，既增加跨氧化层的输运阻力，也降低沿晶界的氧输运能力。Si 氧化后按全溶解近似留下的自由体积，同样进入有效传输性质的描述。不能把“Cr 改变保护性”和“Si 改变传输”并列为彼此独立的物理机制。元素变化对反应速率的影响及氧化消耗的反馈仍保留在耦合方程中。

调研日期：2026-09-14。英文初稿见 [introduction.tex](../drafts/introduction.tex)，排版预览见 [introduction_preview.pdf](../drafts/introduction_preview.pdf)。本版实际引用五篇原始研究，另三篇保留为讨论背景；八篇全文均已落地，出处、阅读位置及证据边界见 [文献清单](../literature/README.md)。以下“本文能做什么”根据当前 `main.tex` 判断；没有运行模型，也没有替你补造未完成的结果。

作者已澄清：长时间氧化前沿的时间序列来自另一篇论文；SiO₂ 全部溶解是模型有意采用的简化，机制依据是 Donghai Du 的 Cr/Si 解耦研究。相应地，时间图需要补齐的是独立出处；SiO₂ 需要说明的是文献机制如何转化为模型近似。这两点不应作为数据不存在或模型引用错误来处理。

建议采用五段，每段完成一个论证任务。

1. **从 304SS 的晶界氧化剂量效应进入。** Deng 2017 的 304NG 实验显示，预辐照剂量增加伴随晶界氧化加深、氧化物 Cr 含量降低。由此提出具体问题：如何从辐照造成的成分变化预测氧传输和前沿推进？研究对象从开头就明确为 304SS。[Deng 2017](https://doi.org/10.1016/j.corsci.2017.08.010)。

2. **连接 RIS、氧化物组成与氧扩散。** Deng 2017/2021 提供 Cr 贫化、Ni/Si 富集及氧化后局部化学的信息。氧化物 Cr 含量改变其对氧扩散的阻力；“保护性”在本文的传输模型中通过有效扩散系数体现。[Deng 2021](https://doi.org/10.1038/s41598-020-80600-x)。

3. **补全决定有效扩散系数的化学与结构因素。** Du 的 Cr/Si 解耦研究为 Si 氧化物溶解、形成孔隙和促进氧传输提供机制依据。这与氧化物 Cr 含量的作用汇入同一个 D_eff。Kuang 2022 的 316L 裂尖显微结果用于支持相关机制，需明确其材料与本文模拟的 304SS 不同。SiO₂ 全部溶解是本文采用的简化，具体体积处理放在 Methods。[Du 2026](https://doi.org/10.1016/j.corsci.2025.113424)，[Kuang 2022](https://doi.org/10.1016/j.corsci.2022.110187)。

4. **把研究问题写成需要建立的定量连接。** Kadambi 2025 已能耦合溶质和点缺陷、预测 RIS。本文进一步连接成分剖面、选择性氧化、氧化物组成与自由体积、D_eff 和氧化动力学。成分、Ni 富集和深度共同用于评估这一耦合。[Kadambi 2025](https://doi.org/10.1016/j.commatsci.2025.113895)。

5. **明确本文模型及检验对象。** 写明 304SS 的 Fe–Cr–Ni–Si 表示、同一 D_eff 同时用于沿晶界和跨氧化层输运、氧化消耗对成分的反馈、分步标定及跨剂量使用统一氧化参数。剂量数据与另一篇论文的时间序列分别对应其来源；时间图的书目信息仍待补齐。同时 RIS 与氧化作为模型可计算的条件简要交代。

Wang 2022/2023 的 316L 结果以及 Lach 2025 的服役 316 研究保留为 Discussion 背景，不作为本版引言的主线或本文 304SS 模型的验证来源。

当前正文有几处会影响引言可信度，需要先处理。

| 位置或说法 | 原文核对 / 模型检查 | 对引言的影响 |
|---|---|---|
| 全文只有 `deng`，且 `refs.bib` 缺失 | 氧化层 Cr 的 74.9、69.5、58.3 at.% 来自 Deng 2017，PDF p. 7；2021 Scientific Reports 是另一篇 APT 工作 | 分设 `deng2017` 和 `deng2021apt`，不要自动将所有 `deng` 替换成同一篇 |
| 0.5/1.5 dpa 时间序列的图注仍用 `deng` | 作者确认来自另一篇论文；其具体书目信息和原图尚待补齐 | 单独对应时间序列来源，不将其误归 Deng 2017，也不擅自认定为 Wang 2023 |
| Si 剖面统一按 1 nm 高斯卷积处理 | Deng 2017 的 1 nm 探针说明针对 TEM/EDX，Fig. 4 展示 Cr/Ni；Deng 2021 则使用 APT | Si 数据需要单独标注来源和测量响应，不能沿用探针直径来证明 APT 的高斯核 |
| 基体 Si = 0.27 at.% | Deng 2017 Table 1 的 0.27 是 **wt.%**；按该表全成分换算，Si 约为 0.53 at.% | 若当前值直接取自该表，就存在单位混用；若来自另一数据集，应给出出处。Cr/Ni 也应使用一致的归一化方式 |
| 氧化后 Ni “随剂量增加” | Deng 2021 的界面富集趋势不能与辐照前的 RIS 富集趋势互换；测量位置也不同 | 不要先把 Ni 描述为统一单调的剂量指标；需要分别说明原始晶界、氧化尖端和侧界面 |
| SiO₂ 全部溶解 | 作者明确采用的模型简化；机制依据为 Du 2026 对 Si 氧化物溶解、孔隙和传输增强的解释 | 保留假设，在 Methods 明确区分机制依据与完全溶解这一理想化处理；引言说明溶解产生的自由体积如何影响 D_eff |
| “fully coupled” 相当于堆内服役 | 方程可以同时开启缺陷源和氧边界条件，但未包含辐解、应力或断裂 | 称“concurrent RIS–oxidation predictions”，不称已验证的堆内 IASCC 预测 |

上述 Si 换算只用于核对原始表的单位，并不是直接建议将模型参数改成 0.53：四元合金简化后是否重新归一化、是否以实测基体值代替名义成分，需要一致说明。

另有两点来自方程本身，决定创新点能写到什么程度。

第一，在采用 SiO₂ 全溶解简化后，无须另求解一套有限速率溶解方程。Methods 应说明该简化的代数实现：Si 消耗对应的等效体积如何计入空隙，以及这部分如何进入厚度和 `D_eff = Σ f_k D_k`。这是让假设可复现的定义问题，不是要求取消假设或增加模型复杂度。

可直接用于 Methods 的表述：

> Motivated by the Si-induced oxide degradation mechanism proposed by Du et al., we assume complete dissolution of the SiO₂ formed during oxidation. Its equivalent volume is retained as free volume contributing to oxygen transport. This approximation represents the effect of silica dissolution without resolving its kinetics explicitly.

第二，仅仅画出近似抛物线的深度曲线不足以证明模型自然识别了限速机制。当前入口传质系数预先设为 `h(t) ∝ t^(-1/2)`，时间趋势会部分受到该边界条件约束。建议用供给阻力、氧化层阻力和反应阻力的比较来支撑限速机制判断。

如果希望进一步量化 Cr 与 Si 的不同作用，可以做保持归一化一致的受控比较：完整 RIS、仅 Cr 变化、仅 Si 变化，并展示它们对深度、氧化层成分、Ni 富集的共同影响。Si 保留与全溶解的比较可作为可选的假设敏感性分析，不是撰写本版引言的前提。这些是后续分析建议，本轮未运行。

现有标题中的 **RIS Controlled** 比现阶段证据强。更稳妥的候选是 *A Mechanistic Model Linking Radiation-Induced Segregation to Grain-Boundary Oxidation Kinetics in 304 Stainless Steel*。若后续受控比较确实证明成分通道主导，再考虑保留 “controlled”。

本轮交付采用独立草稿，没有替换 `main.tex` 或把尚未确认的 `deng` / `du` 引文批量改写。引言引用库为 `literature/introduction.bib`，可单独编译预览；主稿整合时应先逐图解决上表的来源对应关系。
