def checkColunm(doc):
    nid = doc['id_str']
    for i in ['hasHashtag', 'triggerHashtag']:
        if len(doc[i]) == 0:
            ntext = doc['text']
            ncoordinates = doc['coordinates']
            nuser = doc['user']
            ntime = doc['created_at']
            nplace = doc['place']
            nentities = doc['entities']
            sentiment = analyzer.polarity_scores(ntext)
            # swearing = lable_swearing(ntext)
            # topic = give_label(ntext)
            # time_tag = time_label(ntime)
            suburb = give_suburb(ncoordinates)
            hashtag = hasHashtag(ntext)
            triggerHashtag = searchHashtag(tags)
            # generate new tweeter
            ndoc = {'_id': nid, 'text': ntext, 'user': nuser,
                    'coordinates': ncoordinates, 'create_time': ntime,
                    'place': nplace, 'entities': nentities,
                    'addressed': False, 'sentiment': sentiment, 'suburb': suburb, 'hasHashtag': hashtag,
                    'triggerHashtag': triggerHashtag}
            db.save(ndoc)
            print(nid)
            print('********************************************')