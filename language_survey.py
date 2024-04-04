    from survey import AnonyousSurvey

    question = "What's your favourite language ？ "
    language_survrey=AnonyousSurvey(question)

    language_survrey.show_question()
    print('输入q或Q退出调查')
    while True:
        response = input('Language ：')
        if response == 'q' or response == 'Q':
            break
        else:
            language_survrey.store_response(response)

    # print('\nThank you to everyone who participated in the survey')
    # language_survrey.show_results()