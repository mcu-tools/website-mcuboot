---
title: Blog
permalink: /blog/
description: >
    The official MCUboot blog!
flow:
    - row: container_row
      sections:
        - format: custom_include
          source: blog/post_search.html
          payload:
              name: url
              data: /assets/json/posts.json
              category: blog
          # category: News
        - format: custom_include
          source: blog/display_latest_posts.html
          category: blog
---
