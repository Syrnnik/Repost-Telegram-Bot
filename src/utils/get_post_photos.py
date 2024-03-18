def get_post_photos(post):
    post_photos = []
    for attachment in post['attachments']:
        if attachment['type'] == "photo":
            # for photo in attachment['photo']['sizes']:
            #     # if no 'w' use 'z' maybe
            #     if photo['type'] == 'w':
            #         post_photos.append(photo['url'])
            #         break
            post_photos.append(attachment['photo']['sizes'][-1]['url'])
    return post_photos
