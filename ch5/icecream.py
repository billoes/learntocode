def make_sundae(ice_cream='vanillia',sauce='chocolate',nuts=True,
                banana=True, brownies=False,whipped_cream=True):
    recipe = ice_cream+ ' ice cream ' + sauce + ' sauce '           
    if nuts:
        recipe= recipe + 'with nuts and '
    if banana:
        recipe = recipe + 'a banana and '
    if brownies:
        recipe = recipe + 'a brownie and '
    if not whipped_cream:
        recipe = recipe + 'no '
    recipe = recipe + 'whipped cream on top'
    return recipe

sundae = make_sundae()
sundae = make_sundae('chocolate')
sundae = make_sundae(sauce='caramel', whipped_cream=False,banana=False)
print('One sundae coming up with',sundae)

    