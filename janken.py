import random

# じゃんけんの手の定数
GUU = "グー"
CHOKI = "チョキ"
PAA = "パー"

CHOICES = [GUU, CHOKI, PAA]

# 勝敗結果の定数
WIN = "勝ち"
LOSE = "負け"
DRAW = "あいこ"

# 入力値と手のマッピング（数字・ひらがな・カタカナ対応）
INPUT_MAP = {
    "1": GUU,
    "グー": GUU,
    "ぐー": GUU,
    "ぐ": GUU,
    "グ": GUU,
    "2": CHOKI,
    "チョキ": CHOKI,
    "ちょき": CHOKI,
    "ちょ": CHOKI,
    "チョ": CHOKI,
    "3": PAA,
    "パー": PAA,
    "ぱー": PAA,
    "ぱ": PAA,
    "パ": PAA,
}


def get_player_choice():
    """プレイヤーの手を入力して返す。無効な入力は再入力を促す。"""
    while True:
        raw = input("グー(1) / チョキ(2) / パー(3) を入力してください: ").strip()
        choice = INPUT_MAP.get(raw)
        if choice:
            return choice
        print(f"「{raw}」は無効な入力です。グー/チョキ/パー または 1/2/3 を入力してください。")


def get_cpu_choice():
    """CPUの手をランダムに選んで返す。"""
    return random.choice(CHOICES)


# 勝ち判定マップ: プレイヤーの手 -> プレイヤーが勝てるCPUの手
WINS_AGAINST = {
    GUU: CHOKI,
    CHOKI: PAA,
    PAA: GUU,
}


def judge(player, cpu):
    """プレイヤーとCPUの手を比較して勝敗を返す。

    Returns:
        "勝ち" / "負け" / "あいこ"
    """
    if player == cpu:
        return DRAW
    if WINS_AGAINST[player] == cpu:
        return WIN
    return LOSE


def show_result(player, cpu, result):
    """プレイヤーの手・CPUの手・勝敗結果を表示する。"""
    print("---")
    print(f"あなたの手: {player}")
    print(f"CPUの手:    {cpu}")
    print(f"結果: {result}")
    print("---")


def play_again():
    """もう一度プレイするか確認する。y なら True、n なら False を返す。"""
    while True:
        ans = input("もう一度プレイしますか？ (y/n): ").strip().lower()
        if ans == "y":
            return True
        elif ans == "n":
            return False
        print("「y」か「n」を入力してください。")


def show_score(score):
    """ゲーム終了時にスコアサマリーを表示する。"""
    total = sum(score.values())
    win_rate = score[WIN] / total * 100 if total > 0 else 0.0
    print("========== ゲーム終了 ==========")
    print(f"総対戦数: {total}回")
    print(f"勝ち: {score[WIN]}回 / 負け: {score[LOSE]}回 / あいこ: {score[DRAW]}回")
    print(f"勝率: {win_rate:.1f}%")
    print("================================")


def main():
    """ゲームのメインループ。"""
    score = {WIN: 0, LOSE: 0, DRAW: 0}
    try:
        while True:
            player = get_player_choice()
            cpu = get_cpu_choice()
            result = judge(player, cpu)
            show_result(player, cpu, result)
            score[result] += 1
            if not play_again():
                break
    except KeyboardInterrupt:
        print()
    show_score(score)
    print("ゲームを終了します。")


if __name__ == "__main__":
    main()
