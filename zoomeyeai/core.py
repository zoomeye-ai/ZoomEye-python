"""
* Filename: core.py
* Description: cli core function, processing various requests
* Time: 2024.12.05
*/
"""

import os

from zoomeyeai import config, file, show
from zoomeyeai.sdk import ZoomEye

# save zoomeye config folder
zoomeye_dir = os.path.expanduser(config.ZOOMEYE_CONFIG_PATH)


def init_key(key):  # 初始化API密钥并将其保存在本地配置文件中

    """
    initialize through the api key, write the api key to the local configuration file,
    theoretically it will never expire unless you remake the api key
    :param key: user input API key
    :return:
    """
    file.check_exist(zoomeye_dir)
    key = key.strip()
    try:
        zoom = ZoomEye(api_key=key)
    except Exception:
        return
    # api key save path
    key_file = zoomeye_dir + "/apikey"
    # display the remaining resources of the current account
    user_data = zoom.userinfo()
    print(user_data)
    if user_data.get("code") == 60000:
        show.printf("Role: {}".format(user_data.get('data', {}).get('subscription', {}).get('plan', '')))
        show.printf("Points: {}".format(user_data.get('data', {}).get('subscription', {}).get("points", 0)))
        show.printf("Zoomeye Points: {}".format(user_data.get('data', {}).get('subscription', {}).get("zoomeye_points", 0)))
    # save api key
    with open(key_file, 'w') as f:
        f.write(key)
    show.printf("successfully initialized", color="green")
    # change the permission of the configuration file to read-only
    os.chmod(key_file, 0o600)


def init(args):  # 根据用户输入的参数来选择初始化方法，可以通过API密钥来进行初始化
    """
    the initialization processing function will select the initialization method according to the user's input.
    :param args:
    :return:
    """
    api_key = args.apikey
    # use api key init
    if api_key:
        init_key(api_key)
        return
    # invalid parameter
    show.printf("input parameter error!", color="red")
    show.printf("please run <zoomeye init -h> for help.", color="red")


def info(args):  # 打印当前用户的身份和本月剩余的数据配额
    """
    used to print the current identity of the user and the remaining data quota for the month
    :return:
    """
    api_key = file.get_auth_key()
    zm = ZoomEye(api_key=api_key)
    # get user information
    user_response = zm.userinfo()

    if user_response and user_response.get('code') == 60000:
        user_data = user_response.get('data')
        # show in the terminal
        show.printf("username: {}".format(user_data["username"]))
        show.printf("email: {}".format(user_data["email"]))
        show.printf("phone: {}".format(user_data["phone"]))
        show.printf("created_at: {}".format(user_data["created_at"]))
        show.printf("Subscription:: {}".format(user_data["subscription"]))


def search(args):
    dork = args.dork
    page = int(args.page)
    pagesize = int(args.pagesize)
    facets = args.facets
    fields = args.fields
    sub_type = args.sub_type
    figure = args.figure

    api_key = file.get_auth_key()
    zm = ZoomEye(api_key=api_key)
    data = zm.search(dork, page=page, pagesize=pagesize, facets=facets, fields=fields, sub_type=sub_type)

    data_list = data.get('data', [])
    facets_data = data.get('facets', {})
    total = data.get('total', {})

    if len(data_list) > 0:
        keys = data_list[0].keys()
        show.print_filter(",".join(keys), [[i.get(key) for key in keys] for i in data_list])

    if facets_data:
        show.print_facets(facets, facets_data, total, figure, {
            'type': 'type',
            'product': 'product',
            'device': 'device',
            'service': 'service',
            'os': 'os',
            'port': 'port',
            'subdivisions': 'subdivisions',
            'country': 'country',
            'city': 'city',
        })

    # show.printf("please run <zoomeye search -h> for help.")
