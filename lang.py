import tariffs
import config


def eth_address_taken():
    return 'This eth address is already taken.'


def not_registered():
    return 'You are not registered in the system. First, enter the command /start.'


def withdrawals(withdrawals_list):
    if not len(withdrawals_list):
        return 'You have no conclusions yet.'
    withdrawals = 'Your latest findings:\n'
    withdrawals += '\n'.join([f'{withdrawal.amount:.7f} ETH - {withdrawal.created_at}' for withdrawal in withdrawals_list])
    return withdrawals


def top_ups(top_ups_list):
    if not len(top_ups_list):
        return 'You have no recharges yet.'
    top_ups = 'Your latest refills:\n'
    top_ups += '\n'.join([f'{top_up.amount:.7f} ETH - {top_up.created_at}' for top_up in top_ups_list])
    return top_ups


def back_to_main_menu():
    return 'Return to the main menu.'


def balance_transferred_to_user(amount, to_user):
    return f'Amount in {amount:.7f} ETH successfully transferred to user {to_user}.'


def balance_transferred_from_user(amount, from_user):
    return f'User {from_user} ETH has transferred you to the balance {amount} ETH.'


def balance_transferred_to_deposit(amount):
    return f'Amount in {amount:.7f} ETH successfully transferred to deposit.'


def not_approved_previous(amount):
    return f'Your past withdrawal of {amount: .7f} ETH has not yet been approved..' \
           f' You can create a new withdrawal request after the previous one is approved..'


def user_not_registered():
    return 'This user is not registered.'


def not_enough_eth():
    return 'You have insufficient funds. Enter another amount.'


def wrong_command():
    return 'Enter valid command.'


def withdrawal_created(wallet):
    return f'The funds will be transferred to the {wallet} address on the next Wednesday or Sunday.'


def minimal_withdraw_amount():
    return f'The transfer amount must exceed {tariffs.minimal_eth_withdraw()} ETH.'


def partners(user, bot_username, user_invited_by=None):
    partners_info = ''
    if user_invited_by:
        partners_info = f'You were invited by: {user_invited_by}\n'
    referral_link = f'https://telegram.me/{bot_username}?start={str(user.chat_id)}'
    partners_info += f'Your referral link: {referral_link}\n'

    level_percentage = tariffs.get_referral_levels_percentage()

    for idx, percentage in enumerate(level_percentage):
        partners_info += f'Level {idx + 1} - {percentage * 100 * user.deposit_reward}% in a day\n'

    return partners_info


def invalid_input():
    return 'Enter a valid value.'


def wallet_successfully_set(wallet):
    return f'ETH wallet {wallet} has been successfully linked to your account. '


def deposit(user_deposit, user_balance, user_reward, sum_deposit_reward):
    text = f'Deposit: {user_deposit:.7f} ETH. \n'
    if user_deposit >= tariffs.eth_minimal_deposit():
        text += f'Balans: {user_balance:.7f} ETH. \n' \
                f'Edit rate: {user_reward * 100}% in a day.\n'
    else:
        text += f'Initial deposit: {tariffs.eth_minimal_deposit()} ETH\n'
    text += 'Transfer from balance to deposit: /transfer_deposit\n' \
            'Balance transfer to user: /transfer_user'
    return text


def top_up(wallet):
    return f'your wallet: {wallet}\n' \
           'Change ETH wallet address: /wallet\n' \
           f'ETH address for deposit: '


def top_up_invest_wallet():
    return f'*{config.project_eth_address()}*'


def withdraw(wallet):
    return f'your wallet: {wallet}.\n' \
           'Change wallet ETH address: /wallet\n' \
           'Withdrawal: /withdraw'


def wallet_not_set():
    return 'Your withdrawal address is not set.'


def enter_new_wallet():
    return 'Enter the address of your ETH wallet:'


def transfer_balance_to_deposit(balance):
    return f'Your balance: {balance:.7f} ETH.\n' \
           'Enter the amount you want to transfer to the deposit:'


def transfer_balance_to_user(balance):
    return f'Your balance: {balance:.7f} ETH.\n' \
           'Enter the username (alias) of the Telegram and the amount you want to transfer through the space.\n' \
           'for example: "ivan 1.03"'


def create_withdrawal(balance):
    return f'Your balance: {balance:.7f} ETH.\n' \
           'Enter the amount you want to withdraw.:'


def help():
    return 'Has developed[ ](https://telegra.ph/Dobro-pozhalovat-v-ICO-DAY-05-10)' \
           '[BugDeveloper](https://github.com/BugDeveloper)'
