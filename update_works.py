import re

def main():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # Replace logo paths
    html = html.replace('code/src/imports/sxtn_logotype-03.jpg.jpeg', 'sxtn%20logotype-03.jpg.jpeg')

    images = [f'{i}.jpeg' for i in range(1, 12)] + [f'{i}.JPG' for i in range(12, 17)]
    
    desktop_html = '    <div class="works-desktop-container">\n'
    mobile_html = '    <div class="works-mobile">\n'
    
    for i in range(16):
        img = images[i]
        title = f"ARTWORK {i+1:02d}"
        meta = "Experimental Design / 2024"
        
        # Mobile
        mobile_html += f'''      <div class="work-card ar-port"><img src="{img}" alt="{title}" />
        <div class="work-overlay">
          <div>
            <div class="work-overlay-title">{title}</div>
            <div class="work-overlay-meta">{meta}</div>
          </div><svg class="work-arrow" viewBox="0 0 24 24"><line x1="7" y1="17" x2="17" y2="7" /><polyline points="7 7 17 7 17 17" /></svg>
        </div>
      </div>\n'''

    # Desktop
    for group in range(3):
        base = group * 5
        desktop_html += f'''      <div class="works-desktop" style="margin-bottom:1px;">
        <div class="work-card ar-tall" style="grid-row:span 2;">
          <img src="{images[base]}" alt="ARTWORK {base+1:02d}" />
          <div class="work-overlay">
            <div>
              <div class="work-overlay-title">ARTWORK {base+1:02d}</div>
              <div class="work-overlay-meta">Experimental Design / 2024</div>
            </div><svg class="work-arrow" viewBox="0 0 24 24"><line x1="7" y1="17" x2="17" y2="7" /><polyline points="7 7 17 7 17 17" /></svg>
          </div>
        </div>
        <div class="works-right">
          <div class="work-card ar-wide">
            <img src="{images[base+1]}" alt="ARTWORK {base+2:02d}" />
            <div class="work-overlay">
              <div>
                <div class="work-overlay-title">ARTWORK {base+2:02d}</div>
                <div class="work-overlay-meta">Experimental Design / 2024</div>
              </div><svg class="work-arrow" viewBox="0 0 24 24"><line x1="7" y1="17" x2="17" y2="7" /><polyline points="7 7 17 7 17 17" /></svg>
            </div>
          </div>
          <div class="works-bottom-row">
            <div class="work-card ar-square"><img src="{images[base+2]}" alt="ARTWORK {base+3:02d}" />
              <div class="work-overlay">
                <div>
                  <div class="work-overlay-title">ARTWORK {base+3:02d}</div>
                  <div class="work-overlay-meta">Experimental Design / 2024</div>
                </div><svg class="work-arrow" viewBox="0 0 24 24"><line x1="7" y1="17" x2="17" y2="7" /><polyline points="7 7 17 7 17 17" /></svg>
              </div>
            </div>
            <div class="work-card ar-square"><img src="{images[base+3]}" alt="ARTWORK {base+4:02d}" />
              <div class="work-overlay">
                <div>
                  <div class="work-overlay-title">ARTWORK {base+4:02d}</div>
                  <div class="work-overlay-meta">Experimental Design / 2024</div>
                </div><svg class="work-arrow" viewBox="0 0 24 24"><line x1="7" y1="17" x2="17" y2="7" /><polyline points="7 7 17 7 17 17" /></svg>
              </div>
            </div>
            <div class="work-card ar-square"><img src="{images[base+4]}" alt="ARTWORK {base+5:02d}" />
              <div class="work-overlay">
                <div>
                  <div class="work-overlay-title">ARTWORK {base+5:02d}</div>
                  <div class="work-overlay-meta">Experimental Design / 2024</div>
                </div><svg class="work-arrow" viewBox="0 0 24 24"><line x1="7" y1="17" x2="17" y2="7" /><polyline points="7 7 17 7 17 17" /></svg>
              </div>
            </div>
          </div>
        </div>
      </div>\n'''
      
    # Group 4 (1 item)
    desktop_html += f'''      <div class="works-desktop">
        <div class="work-card ar-wide" style="grid-column: span 2;">
          <img src="{images[15]}" alt="ARTWORK 16" />
          <div class="work-overlay">
            <div>
              <div class="work-overlay-title">ARTWORK 16</div>
              <div class="work-overlay-meta">Experimental Design / 2024</div>
            </div><svg class="work-arrow" viewBox="0 0 24 24"><line x1="7" y1="17" x2="17" y2="7" /><polyline points="7 7 17 7 17 17" /></svg>
          </div>
        </div>
      </div>\n'''
      
    desktop_html += '    </div>'
    mobile_html += '    </div>'

    # Replace the desktop and mobile works sections
    # Find the start and end of works-desktop
    desktop_pattern = re.compile(r'<!-- Desktop -->.*?<!-- Mobile -->', re.DOTALL)
    html = desktop_pattern.sub(f'<!-- Desktop -->\n{desktop_html}\n\n    <!-- Mobile -->', html)
    
    mobile_pattern = re.compile(r'<!-- Mobile -->.*?(?=\n\s*<div class="works-count">)', re.DOTALL)
    html = mobile_pattern.sub(f'<!-- Mobile -->\n{mobile_html}', html)
    
    # Change "5 projects shown" to "16 projects shown"
    html = html.replace('5 projects shown', '16 projects shown')

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)

if __name__ == "__main__":
    main()
