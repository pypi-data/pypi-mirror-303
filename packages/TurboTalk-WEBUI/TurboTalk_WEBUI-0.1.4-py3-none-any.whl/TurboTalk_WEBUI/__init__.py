from .app import set_bot_name, set_company_name, main

def start_webui_chat(bot_name, company_name): 
    set_bot_name(bot_name)
    set_company_name(company_name)
    main()
