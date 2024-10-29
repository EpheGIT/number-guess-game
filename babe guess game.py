import random

def check_special_number(mid):
    """检查是否是彩蛋数字并输出相应信息"""
    if mid == 520:
        return "💖 宝宝心中的数字是 520～我也爱你～❤️"
    elif mid == 817:
        return "🎉 宝宝心中的数字是 817！哇塞是我的生日🎂！爱你宝贝～🎈"
    elif mid == 412:
        return "🎂 宝宝生日每天快乐哦🎉！希望你的每一天都像今天一样幸福～"
    else:
        return f"✨ 宝宝心中的数字是 {mid}～❤️"

def guess_number_game():
    while True:
        print("\n🎲 欢迎我的宝宝程雨濛来到猜数字游戏！💞")
        print("亲爱的bb，请在心里想一个 1 到 1000 之间的数字，👀 你的老公会在 10 次机会内猜到它～")
        input("🌟 准备好了我们就按回车开始吧！")

        low, high = 1, 1000

        # 第一步随机猜测
        while True:
            mid = random.randint(low, high)
            print(f"\n🤔 你的老公先来试一个数字 {mid}，对吗？")
            response = input("请输入 (h: 高了, l: 低了, c: 猜对了): ").strip().lower()

            if response == 'c':
                print(check_special_number(mid))
                break
            elif response == 'h':
                high = mid - 1
                break
            elif response == 'l':
                low = mid + 1
                break
            else:
                print("🔍 宝宝请输入正确的指令～：'h'、'l' 或 'c'")

        # 正式的十次二分查找
        attempts = 0
        max_attempts = 10

        while attempts < max_attempts and low <= high:
            # 检查是否只剩下一个可能的数字
            if low == high:
                print("\n" + check_special_number(low))
                break

            mid = (low + high) // 2
            attempts += 1

            # 第十次尝试直接输出结果
            if attempts == max_attempts:
                print("\n" + check_special_number(mid))
                break

            print(f"\n🔮 第 {attempts} 次尝试：我猜是 {mid}，对吗？")
            response = input("请输入 (h: 高了, l: 低了, c: 猜对啦): ").strip().lower()

            if response == 'c':
                print("\n" + check_special_number(mid))
                break
            elif response == 'h':
                high = mid - 1
                print(f"😮 好嘛，{mid} 高了的话，我会继续在 ({low}, {high}) 范围内找。")
            elif response == 'l':
                low = mid + 1
                print(f"😌 嗯嗯，{mid} 既然低了，我会继续在 ({low}, {high}) 范围内找。")
            else:
                print("🔍 宝宝请输入正确的字母～，请输入 'h'、'l' 或 'c'。")
                attempts -= 1  # 无效输入不计入尝试次数

        # 游戏结束后询问是否继续
        replay = input("\n🎉 被我猜到啦！还要继续玩吗？(y: 继续, n: 退出): ").strip().lower()
        if replay != 'y':
            print("💖 宝宝iloveu~！期待下次再和你一起猜数字！🥰")
            break

# 运行游戏
guess_number_game()
