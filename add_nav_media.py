# Run this from your Corporate Retreat folder:
# python3 add_nav_media.py

with open('media.html', 'r') as f:
    content = f.read()

nav_css = """
  .site-nav { background: var(--ocean); display: flex; justify-content: center; padding: 0; position: sticky; top: 0; z-index: 100; }
  .site-nav a { color: rgba(255,255,255,0.7); text-decoration: none; font-family: 'Jost', sans-serif; font-size: 0.65rem; font-weight: 600; letter-spacing: 3px; text-transform: uppercase; padding: 14px 16px; transition: color 0.15s, background 0.15s; }
  .site-nav a:hover { color: white; background: rgba(255,255,255,0.08); }
  .site-nav a.active { color: white; border-bottom: 2px solid rgba(255,255,255,0.5); }
  @media (max-width: 520px) { .site-nav a { padding: 12px 9px; font-size: 0.58rem; letter-spacing: 1.5px; } }
"""

nav_html = '<nav class="site-nav"><a href="index.html">Home</a><a href="itinerary_1.html">Itinerary</a><a href="sharkhouse_rooms.html">Rooms</a><a href="https://sharkhousenj.com/welcome/tiger" target="_blank">Tiger</a><a href="https://sharkhousenj.com/welcome/mako" target="_blank">Mako</a><a href="media.html" class="active">Media</a></nav>\n'

content = content.replace('</style>', nav_css + '</style>', 1)
content = content.replace('<body>', '<body>\n' + nav_html, 1)

with open('media.html', 'w') as f:
    f.write(content)

print("media.html updated with nav!")
