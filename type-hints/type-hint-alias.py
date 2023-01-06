from typing import TypeAlias


# define the type for PostsType
# PostsType: TypeAlias = dict[int, str]       # this is using the TypeAlias module
PostsType = dict[int, str]                  # this will also work (not using TypeAlias module)

# now you can define new variables with PostsType as type
new_posts: PostsType = {1: 'Genifer 1', 2: 'Genifer 2'}
old_posts: PostsType = {1: 'Old Genifer'}


new_posts[3] = 'Genifer 3'
new_posts['new'] = 'Genifer new'        # this will generate a warning from IDE
                                        # Expected type 'int'

print(new_posts)

