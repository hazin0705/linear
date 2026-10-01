import numpy as np
import matplotlib.pyplot as plt

#x1의 범위

x1 = np.linspace(-2,3,500)

# 식 작성
x2_eq1 = 3-2*x1

x2_eq2 = 2*x1 -1

x2_eq3 = (x1+1)/2

#그래프 생성
plt.figure(figsize=(8,7))

plt.plot(
    x1, x2_eq1,
    color="deeppink",
    linewidth=2.5,
    label=r"$2x_1+x_2=3$"
)

plt.plot(
    x1, x2_eq2,
    color="dodgerblue",
    linewidth=2.5,
    label=r"$2x_1-x_2=1$"
)

plt.plot(
    x1, x2_eq3,
    color="seagreen",
    linewidth=2.5,
    label=r"$x_1-2x_2=-1$"
)

#세 직선의 공통해
solution_x1 = 1
solution_x2 = 1

plt.scatter(
    solution_x1,
    solution_x2,
    color = "black",
    s=70,
    zorder=5
)


plt.annotate(
    r"$(1,1)$",
    xy=(solution_x1,solution_x2),
    xytext = (1.15,1.2),
    fontsize = 14
)

plt.plot(
    [solution_x1,solution_x1],
    [0,solution_x2],
    color = "deeppink",
    linestyle = "--",
    linewidth=1
)

plt.plot(
    [0,solution_x1],
    [solution_x2,solution_x2],
    color = "deeppink",
    linestyle = "--",
    linewidth=1
)

#x축 y축

plt.axhline(0, color = "black",linewidth =1)
plt.axvline(0, color = "black",linewidth =1)

#그래프 설정
plt.xlim(-2,3)
plt.ylim(-3,5)
plt.xlabel(r"$x_1", fontsize=14)
plt.ylabel(r"$x_2$", fontsize =14,rotation=0,labelpad=15)
plt.title("Three Linear Equations", fontsize=16)
plt.grid(alpha=0.25)
plt.legend(fontsize=12)
plt.gca().set_aspect("equal",adjustable="box")

plt.tight_layout()
plt.show()
