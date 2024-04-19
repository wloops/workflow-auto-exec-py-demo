from playwright.sync_api import sync_playwright


def login(url, username, password):
    # 启动 playwright driver 进程
    p = sync_playwright().start()

    # 启动浏览器，返回 Browser 类型对象
    browser = p.chromium.launch(headless=False, args=["--start-maximized"])

    # 创建新页面，返回 Page 类型对象
    page = browser.new_page(no_viewport=True)

    page.goto(url)
    # print(page.title())  # 打印网页标题栏
    page.locator('#userID').fill(username)
    page.locator('#hisu_password').fill(password)
    page.locator('#submit').click()

    page.wait_for_timeout(1000)

    page.locator('#taskSetting').click()
    # 绑定当前标签页
    this_page = page.locator('.page.unitBox[style="display: block;"]')

    return page, this_page, p

