about_top_template = open('templates/about_top.html').read()

about_content = open('content/about_index.html').read()

about_html = about_top_template + about_content
open('docs/about.html', 'w+').write(about_html)


#cat templates/about_top.html content/about_index.html > docs/about_index.html

#cat templates/contact_top.html content/contact_index.html > docs/contact_index.html

#cat templates/belgium_top.html content/belgium_index.html > docs/belgium_index.html

#cat templates/bhutan_top.html content/bhutan_index.html > docs/bhutan_index.html

#cat templates/egypt_top.html content/egypt_index.html > docs/egypt_index.html

#cat templates/india_top.html content/india_index.html > docs/india_index.html

#cat templates/ireland_top.html content/ireland_index.html > docs/ireland_index.html

#cat templates/slovenia_top.html content/slovenia_index.html > docs/slovenia_index.html

#cat templates/spain_top.html content/spain_index.html > docs/spain_index.html

#cat templates/uzbekistan_top.html content/uzbekistan_index.html > docs/uzbekistan_index.html

#cat templates/vietnam_top.html content/vietnam_index.html > docs/vietnam_index.html
