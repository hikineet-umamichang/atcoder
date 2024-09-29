import random
import math


def objective_function(solution):
    """
    目的関数: 与えられた解（solution）の評価値を計算する関数。
    問題に応じて実装を変更してください。
    """
    # Example: 二次関数の最小化
    return sum(x**2 for x in solution)


def neighbor_function(solution):
    """
    隣接解を生成する関数: 現在の解(solution)に対して
    ランダムに微小な変更を加えた新しい解を生成します。
    """
    neighbor = solution[:]
    index = random.randint(0, len(solution) - 1)
    # ランダムに一つの要素を微小に変更
    neighbor[index] += random.uniform(-1, 1)
    return neighbor


def acceptance_probability(old_cost, new_cost, temperature):
    """
    受容確率を計算する関数: 新しい解をどの程度の確率で受容するかを決定します。
    コストが低い場合は無条件で受容し、コストが高い場合でも確率的に受容します。
    """
    if new_cost < old_cost:
        return 1.0
    return math.exp((old_cost - new_cost) / temperature)


def simulated_annealing(initial_solution, initial_temp, cooling_rate, max_iter):
    """
    焼きなまし法のメイン関数: 焼きなまし法を実行し、最適な解を探索します。
    """
    current_solution = initial_solution
    current_cost = objective_function(current_solution)
    best_solution = current_solution[:]
    best_cost = current_cost
    temperature = initial_temp

    for i in range(max_iter):
        new_solution = neighbor_function(current_solution)
        new_cost = objective_function(new_solution)

        if (
            acceptance_probability(current_cost, new_cost, temperature)
            > random.random()
        ):
            current_solution = new_solution
            current_cost = new_cost

            # 最良解を更新
            if current_cost < best_cost:
                best_solution = current_solution[:]
                best_cost = current_cost

        # 温度を冷却
        temperature *= cooling_rate

        # 任意: 進捗を表示
        if i % 100 == 0:
            print(
                f"Iteration {i}: Best Cost = {best_cost:.4f}, Current Temp = {temperature:.4f}"
            )

    return best_solution, best_cost


# パラメータ設定
initial_solution = [
    random.uniform(-10, 10) for _ in range(5)
]  # 初期解（例として5次元ベクトル）
initial_temp = 1000  # 初期温度
cooling_rate = 0.99  # 冷却率（温度が減少する割合）
max_iter = 10000  # 最大反復回数

# 焼きなまし法の実行
best_solution, best_cost = simulated_annealing(
    initial_solution, initial_temp, cooling_rate, max_iter
)

print("Best Solution:", best_solution)
print("Best Cost:", best_cost)
