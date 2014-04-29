vi-like keyboard navigation on Trac ITS
=======================================

# description

You can navigate with `j` or `k` keys between rows
on report, query, timeline, search results, ticket, and so on.

* `j` or down arrow ... select a next item
* `k` or up arrow ... select a previous item
* `v` or Enter ... open selected item

* `h` or `0` ... select a first item
* `g` ... select a last item

* `/` ... focus global search bar

* `p` ... pin selected item
* `o` ... open pinned items, or selected item if no item are pinned

# how to install this plugin to trac

1. `easy_install https://github.com/matobaa/Trac-LDRizePlugin/tarball/trunk`
2. restart your trac server
3. enable LDize at admin/plugin panel
