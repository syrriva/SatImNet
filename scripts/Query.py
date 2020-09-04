def Query(tree, condition, flagpath=''):
    def SeekLeaf(tree, condition, flagpath='', query=None):
        if query is None:
            query = []
        obj = ['branch', 'zipfile', 'leaf']
        if type(tree) == dict:
            if tree['type'] == 'file':
                keys = list(condition.keys())
                flag = True
                for k in keys:
                    if k == 'class' and len(tree[k]) > 0 and len(condition[k]) == 0:
                        flag = False
                        break
                    elif k == 'class' and len(condition[k]) != len(list(set(tree[k]) & set(condition[k]))):
                        flag = False
                        break
                    elif k == 'size' and type(condition[k]) == list and len(condition[k]) == 2:
                        if tree[k] < condition[k][0] or tree[k] > condition[k][1]:
                            flag = False
                            break
                    elif 'metainfo' in k:
                        k2 = k.split('_')[1]
                        if k2 in ['numofbands', 'rows', 'columns'] and type(condition[k]) == list and len(condition[k]) == 2:
                            if tree['metainfo'][k2] < condition[k][0] or tree['metainfo'][k2] > condition[k][1]:
                                flag = False
                                break
                        elif condition[k] != tree['metainfo'][k2]:
                            flag = False
                            break
                    elif k == 'path' and type(condition[k]) == str:
                        if not condition[k] in tree[k]:
                            flag = False
                            break
                    elif k == 'name':
                        if not condition[k] in tree[k]:
                            flag = False
                            break
                    elif k != 'class' and condition[k] != tree[k]:
                        flag = False
                        break
                if flag:
                    if 'path' in flagpath:
                        query.append(tree['path'])
                    else:
                        query.append(tree)
            else:
                for t in obj:
                    if len(tree[t]) > 0:
                        query = SeekLeaf(tree[t], condition, flagpath, query)
        elif type(tree) == list and len(tree) > 0:
            for elem in range(len(tree)):
                query = SeekLeaf(tree[elem], condition, flagpath, query)
        return query
    query = SeekLeaf(tree, condition, flagpath, [])
    if flagpath != 'path_v':
        print('Found %d record%s.' % (len(query), '' if len(query)==1 else 's'))
    return query
