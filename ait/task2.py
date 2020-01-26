"""task 2 / time 17:45.3 """


def collect_names(mails):
    unique_names = []
    start_phrase = "Subject: "
    end_phrase = " viewed the document"
    for mail in mails:
        target = mail.find(end_phrase)
        if target != -1:
            unique_names.append(mail[(mail.find(start_phrase) + len(start_phrase)): target])
        else:
            continue
    return list(set(unique_names))


if __name__ == "__main__":
    mails = [
        'Sep 30, 2019. From: Robot. Subject: John Doe viewed the document. 123',
        'Oct 15, 2019. To: me. Subject: Spam. Spam',
        'Dec 2, 2019. From: Robot. To: me. Subject: Vasya Pupkin viewed the document. Please sign',
        'Dec 15, 2019. Subject: The truth is out there',
        'Dec 25, 2019. Subject: Merry Christmas!',
        'Jan 10, 2020. Subject: Fox Mulder viewed the document. Please check',
        'Jan 12, 2020. Subject: John Doe viewed the document. Great news...'
    ]  # task data
    print(collect_names(mails))