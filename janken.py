import random

# じゃんけんの手の定数
GUU = "グー"
CHOKI = "チョキ"
PAA = "パー"

CHOICES = [GUU, CHOKI, PAA]

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


def main():
    """ゲームのメインループ。"""
    while True:
        player = get_player_choice()
        cpu = random.choice(CHOICES)
        if player == cpu:
            result = "あいこ"
        elif (player == GUU and cpu == CHOKI) or (player == CHOKI and cpu == PAA) or (player == PAA and cpu == GUU):
            result = "勝ち"
        else:
            result = "負け"
        show_result(player, cpu, result)
        if not play_again():
            print("ゲームを終了します。")
            break


if __name__ == "__main__":
    main()
