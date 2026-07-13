<svg width="1180" height="610" viewBox="0 0 1180 610" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <filter id="noise">
      <feTurbulence type="fractalNoise" baseFrequency="0.65" numOctaves="3" stitchTiles="stitch" />
      <feColorMatrix type="matrix" values="1 0 0 0 0, 0 1 0 0 0, 0 0 1 0 0, 0 0 0 0.05 0" />
    </filter>

    <linearGradient id="accent-gradient" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#7C3AED" />
      <stop offset="50%" stop-color="#22D3EE" />
      <stop offset="100%" stop-color="#10B981" />
      <animate attributeName="x1" values="0%;100%;0%" dur="10s" repeatCount="indefinite" />
      <animate attributeName="y1" values="0%;100%;0%" dur="10s" repeatCount="indefinite" />
    </linearGradient>

    <linearGradient id="ascii-gradient" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#06B6D4" />
      <stop offset="100%" stop-color="#8B5CF6" />
      <animate attributeName="x1" values="0%;100%;0%" dur="8s" repeatCount="indefinite" />
      <animate attributeName="x2" values="100%;0%;100%" dur="8s" repeatCount="indefinite" />
    </linearGradient>

    <radialGradient id="bg-glow-1" cx="20%" cy="30%" r="50%">
      <stop offset="0%" stop-color="#22D3EE" stop-opacity="0.15" />
      <stop offset="100%" stop-color="#030712" stop-opacity="0" />
    </radialGradient>

    <radialGradient id="bg-glow-2" cx="80%" cy="80%" r="50%">
      <stop offset="0%" stop-color="#7C3AED" stop-opacity="0.15" />
      <stop offset="100%" stop-color="#030712" stop-opacity="0" />
    </radialGradient>
    
    <radialGradient id="bg-glow-3" cx="50%" cy="50%" r="40%">
      <stop offset="0%" stop-color="#10B981" stop-opacity="0.1" />
      <stop offset="100%" stop-color="#030712" stop-opacity="0" />
    </radialGradient>

    <filter id="glass-blur" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="12" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>

    <filter id="glow-strong">
      <feGaussianBlur stdDeviation="4" result="coloredBlur"/>
      <feMerge>
        <feMergeNode in="coloredBlur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>

    <clipPath id="panel-clip">
      <rect x="0" y="0" width="1180" height="610" rx="24" />
    </clipPath>

    <clipPath id="type-clip-1">
      <rect x="0" y="-20" width="0" height="30">
        <animate attributeName="width" values="0;200;200;0;0" keyTimes="0; 0.05; 0.15; 0.20; 1" dur="15s" repeatCount="indefinite" />
      </rect>
    </clipPath>
    <clipPath id="type-clip-2">
      <rect x="0" y="-20" width="0" height="30">
        <animate attributeName="width" values="0;0;220;220;0;0" keyTimes="0; 0.20; 0.25; 0.35; 0.40; 1" dur="15s" repeatCount="indefinite" />
      </rect>
    </clipPath>
    <clipPath id="type-clip-3">
      <rect x="0" y="-20" width="0" height="30">
        <animate attributeName="width" values="0;0;260;260;0;0" keyTimes="0; 0.40; 0.45; 0.55; 0.60; 1" dur="15s" repeatCount="indefinite" />
      </rect>
    </clipPath>
    <clipPath id="type-clip-4">
      <rect x="0" y="-20" width="0" height="30">
        <animate attributeName="width" values="0;0;150;150;0;0" keyTimes="0; 0.60; 0.65; 0.75; 0.80; 1" dur="15s" repeatCount="indefinite" />
      </rect>
    </clipPath>
    <clipPath id="type-clip-5">
      <rect x="0" y="-20" width="0" height="30">
        <animate attributeName="width" values="0;0;160;160;0" keyTimes="0; 0.80; 0.85; 0.95; 1" dur="15s" repeatCount="indefinite" />
      </rect>
    </clipPath>

    <clipPath id="ascii-clip">
      <rect x="0" y="0" width="400" height="0">
        <animate attributeName="height" values="0;450;450" keyTimes="0; 0.3; 1" dur="4s" fill="freeze" />
      </rect>
    </clipPath>
  </defs>

  <rect width="100%" height="100%" fill="#030712" />
  
  <circle cx="20%" cy="30%" r="600" fill="url(#bg-glow-1)">
    <animate attributeName="cx" values="20%;30%;20%" dur="20s" repeatCount="indefinite" />
    <animate attributeName="cy" values="30%;40%;30%" dur="25s" repeatCount="indefinite" />
  </circle>
  <circle cx="80%" cy="80%" r="600" fill="url(#bg-glow-2)">
    <animate attributeName="cx" values="80%;70%;80%" dur="22s" repeatCount="indefinite" />
    <animate attributeName="cy" values="80%;60%;80%" dur="28s" repeatCount="indefinite" />
  </circle>
  <circle cx="50%" cy="50%" r="500" fill="url(#bg-glow-3)">
    <animate attributeName="r" values="400;500;400" dur="15s" repeatCount="indefinite" />
  </circle>

  <g fill="#22D3EE" opacity="0.3">
    <circle cx="100" cy="500" r="2">
      <animate attributeName="cy" values="500;100" dur="15s" repeatCount="indefinite" />
      <animate attributeName="opacity" values="0;0.5;0" dur="15s" repeatCount="indefinite" />
    </circle>
    <circle cx="900" cy="600" r="1.5">
      <animate attributeName="cy" values="600;200" dur="20s" repeatCount="indefinite" />
      <animate attributeName="opacity" values="0;0.6;0" dur="20s" repeatCount="indefinite" />
    </circle>
    <circle cx="500" cy="400" r="2.5">
      <animate attributeName="cy" values="400;50" dur="12s" repeatCount="indefinite" />
      <animate attributeName="opacity" values="0;0.4;0" dur="12s" repeatCount="indefinite" />
    </circle>
    <circle cx="1100" cy="300" r="2">
      <animate attributeName="cy" values="300;0" dur="18s" repeatCount="indefinite" />
      <animate attributeName="opacity" values="0;0.5;0" dur="18s" repeatCount="indefinite" />
    </circle>
  </g>

  <rect width="100%" height="100%" filter="url(#noise)" opacity="0.4" style="mix-blend-mode: overlay;" />

  <g transform="translate(30, 30)">
    <rect x="0" y="0" width="1120" height="550" rx="20" fill="#0F172A" fill-opacity="0.5" filter="url(#glass-blur)" />
    
    <rect x="0" y="0" width="1120" height="550" rx="20" fill="none" stroke="rgba(255,255,255,0.08)" stroke-width="1.5" />
    <rect x="0" y="0" width="1120" height="550" rx="20" fill="none" stroke="url(#accent-gradient)" stroke-width="1.5" opacity="0.4" clip-path="url(#panel-clip)">
      <animate attributeName="opacity" values="0.1;0.5;0.1" dur="6s" repeatCount="indefinite" />
    </rect>

    <g transform="translate(40, 60)">
      <animateTransform attributeName="transform" type="translate" values="40,60; 40,50; 40,60" dur="6s" repeatCount="indefinite" />
      
      <circle cx="160" cy="180" r="150" fill="url(#ascii-gradient)" opacity="0.15" filter="url(#glow-strong)">
        <animate attributeName="r" values="130;160;130" dur="4s" repeatCount="indefinite" />
      </circle>

      <g clip-path="url(#ascii-clip)">
        <text x="0" y="0" font-family="monospace" font-size="12" font-weight="bold" fill="url(#ascii-gradient)" style="white-space: pre;" letter-spacing="1.5">
          <tspan x="0" dy="1.2em">              _,.-------.,_              </tspan>
          <tspan x="0" dy="1.2em">          ,;~'             '~;,          </tspan>
          <tspan x="0" dy="1.2em">        ,;                     ;,        </tspan>
          <tspan x="0" dy="1.2em">       ;                         ;       </tspan>
          <tspan x="0" dy="1.2em">      ,'                         ',      </tspan>
          <tspan x="0" dy="1.2em">     ,;                           ;,     </tspan>
          <tspan x="0" dy="1.2em">     ; ;      .           .      ; ;     </tspan>
          <tspan x="0" dy="1.2em">     | ;   ______       ______   ; |     </tspan>
          <tspan x="0" dy="1.2em">     |  `/~"     ~" . "~     "~\'  |     </tspan>
          <tspan x="0" dy="1.2em">     |  ~  ,-~~~^~, | ,~^~~~-,  ~  |     </tspan>
          <tspan x="0" dy="1.2em">      |   |        }:{        |   |      </tspan>
          <tspan x="0" dy="1.2em">      |   l       / | \       !   |      </tspan>
          <tspan x="0" dy="1.2em">      .~  (__,.--" .^. "--.,__)  ~.      </tspan>
          <tspan x="0" dy="1.2em">      |     ---;' / | \ `;---     |      </tspan>
          <tspan x="0" dy="1.2em">       \__.       \/^\/       .__/       </tspan>
          <tspan x="0" dy="1.2em">        V| \                 / |V        </tspan>
          <tspan x="0" dy="1.2em">         | |T~\___!___!___/~T| |         </tspan>
          <tspan x="0" dy="1.2em">         | |`IIII_I_I_I_IIII'| |         </tspan>
          <tspan x="0" dy="1.2em">         |  \,III I I I III,/  |         </tspan>
          <tspan x="0" dy="1.2em">          \   `~~~~~~~~~~'    /          </tspan>
          <tspan x="0" dy="1.2em">            \   .       .   /            </tspan>
          <tspan x="0" dy="1.2em">              \.    ^    ./              </tspan>
          <tspan x="0" dy="1.2em">                ^~~~^~~~^                </tspan>
        </text>
      </g>

      <rect x="0" y="0" width="350" height="2" fill="url(#ascii-gradient)" opacity="0.6">
        <animate attributeName="y" values="0; 350; 0" dur="8s" repeatCount="indefinite" />
        <animate attributeName="opacity" values="0;0.8;0" dur="8s" repeatCount="indefinite" />
      </rect>
    </g>

    <g transform="translate(420, 40)">
      
      <g transform="translate(0, 0)">
        <circle cx="10" cy="10" r="6" fill="#EF4444" opacity="0.8" />
        <circle cx="30" cy="10" r="6" fill="#F59E0B" opacity="0.8" />
        <circle cx="50" cy="10" r="6" fill="#10B981" opacity="0.8" />
        <text x="75" y="14" font-family="sans-serif" font-size="12" fill="#94A3B8" font-weight="500" letter-spacing="1">guest@abhinand: ~</text>
      </g>

      <line x1="0" y1="30" x2="660" y2="30" stroke="rgba(255,255,255,0.05)" stroke-width="1" />

      <g transform="translate(0, 70)" font-family="sans-serif">
        
        <text x="0" y="0" font-size="36" font-weight="800" fill="#F8FAFC" letter-spacing="-0.5">
          Hi 👋 I'm <tspan fill="url(#accent-gradient)">Abhinand SD</tspan>
        </text>

        <g transform="translate(0, 45)" font-family="monospace" font-size="20" font-weight="600">
          <text x="0" y="0" fill="#94A3B8">&gt; </text>
          
          <g transform="translate(20, 0)">
            <text x="0" y="0" fill="#22D3EE" clip-path="url(#type-clip-1)">Software Engineer</text>
            <text x="0" y="0" fill="#7C3AED" clip-path="url(#type-clip-2)">Full Stack Developer</text>
            <text x="0" y="0" fill="#10B981" clip-path="url(#type-clip-3)">Open Source Contributor</text>
            <text x="0" y="0" fill="#06B6D4" clip-path="url(#type-clip-4)">UI Engineer</text>
            <text x="0" y="0" fill="#8B5CF6" clip-path="url(#type-clip-5)">AI Enthusiast</text>
            
            <text x="0" y="0" fill="#F8FAFC">
              <animate attributeName="x" values="180; 220; 250; 120; 140" keyTimes="0; 0.2; 0.4; 0.6; 0.8" dur="15s" repeatCount="indefinite" />
              |
              <animate attributeName="opacity" values="1;0;1" dur="0.8s" repeatCount="indefinite" />
            </text>
          </g>
        </g>

        <g transform="translate(0, 100)" font-size="15" font-family="monospace" fill="#94A3B8">
          <g opacity="0">
            <animate attributeName="opacity" values="0;1;1" keyTimes="0; 0.1; 1" dur="2s" fill="freeze" />
            <text x="0" y="0">Location: <tspan fill="#F8FAFC">Banglore</tspan></text>
          </g>
          <g opacity="0">
            <animate attributeName="opacity" values="0;1;1" keyTimes="0; 0.1; 1" begin="0.3s" dur="2s" fill="freeze" />
            <text x="0" y="25">Education:<tspan fill="#F8FAFC"> B.Tech CSE</tspan></text>
          </g>
          <g opacity="0">
            <animate attributeName="opacity" values="0;1;1" keyTimes="0; 0.1; 1" begin="0.6s" dur="2s" fill="freeze" />
            <text x="0" y="50">Focus:    <tspan fill="#F8FAFC"> Software development</tspan></text>
          </g>
          <g opacity="0">
            <animate attributeName="opacity" values="0;1;1" keyTimes="0; 0.1; 1" begin="0.9s" dur="2s" fill="freeze" />
            <text x="0" y="75">Portfolio:<tspan fill="#22D3EE"> https://abhinandsdin.vercel.app/</tspan></text>
          </g>
          <g opacity="0">
            <animate attributeName="opacity" values="0;1;1" keyTimes="0; 0.1; 1" begin="1.2s" dur="2s" fill="freeze" />
            <text x="0" y="100">Email:    <tspan fill="#F8FAFC"> abhinandsd49@gmail.com</tspan></text>
          </g>
        </g>

        <g transform="translate(0, 245)">
          <text x="0" y="0" font-size="14" font-weight="bold" fill="#F8FAFC" letter-spacing="1" opacity="0">
            <animate attributeName="opacity" values="0;1;1" keyTimes="0; 0.1; 1" begin="1.5s" dur="2s" fill="freeze" />
            TECH STACK
          </text>
          
          <g transform="translate(0, 15)" font-size="13" font-family="sans-serif" font-weight="600" opacity="0">
            <animate attributeName="opacity" values="0;1;1" keyTimes="0; 0.1; 1" begin="1.8s" dur="2s" fill="freeze" />
            
            <g transform="translate(0, 0)">
              <rect x="0" y="0" width="70" height="30" rx="15" fill="rgba(255,255,255,0.03)" stroke="rgba(255,255,255,0.1)"/>
              <text x="35" y="19" fill="#E2E8F0" text-anchor="middle">React</text>

              <rect x="80" y="0" width="80" height="30" rx="15" fill="rgba(255,255,255,0.03)" stroke="rgba(255,255,255,0.1)"/>
              <text x="120" y="19" fill="#E2E8F0" text-anchor="middle">Next.js</text>

              <rect x="170" y="0" width="80" height="30" rx="15" fill="rgba(255,255,255,0.03)" stroke="rgba(255,255,255,0.1)"/>
              <text x="210" y="19" fill="#E2E8F0" text-anchor="middle">Node.js</text>

              <rect x="260" y="0" width="105" height="30" rx="15" fill="rgba(255,255,255,0.03)" stroke="rgba(255,255,255,0.1)"/>
              <text x="312.5" y="19" fill="#E2E8F0" text-anchor="middle">TypeScript</text>
              
              <rect x="375" y="0" width="85" height="30" rx="15" fill="rgba(255,255,255,0.03)" stroke="rgba(255,255,255,0.1)"/>
              <text x="417.5" y="19" fill="#E2E8F0" text-anchor="middle">Tailwind</text>
            </g>

            <g transform="translate(0, 40)">
              <rect x="0" y="0" width="75" height="30" rx="15" fill="rgba(255,255,255,0.03)" stroke="rgba(255,255,255,0.1)"/>
              <text x="37.5" y="19" fill="#E2E8F0" text-anchor="middle">Python</text>

              <rect x="85" y="0" width="75" height="30" rx="15" fill="rgba(255,255,255,0.03)" stroke="rgba(255,255,255,0.1)"/>
              <text x="122.5" y="19" fill="#E2E8F0" text-anchor="middle">Docker</text>

              <rect x="170" y="0" width="85" height="30" rx="15" fill="rgba(255,255,255,0.03)" stroke="rgba(255,255,255,0.1)"/>
              <text x="212.5" y="19" fill="#E2E8F0" text-anchor="middle">Postgres</text>

              <rect x="265" y="0" width="60" height="30" rx="15" fill="rgba(255,255,255,0.03)" stroke="rgba(255,255,255,0.1)"/>
              <text x="295" y="19" fill="#E2E8F0" text-anchor="middle">AWS</text>

              <rect x="335" y="0" width="50" height="30" rx="15" fill="rgba(255,255,255,0.03)" stroke="rgba(255,255,255,0.1)"/>
              <text x="360" y="19" fill="#E2E8F0" text-anchor="middle">Git</text>

              <rect x="395" y="0" width="65" height="30" rx="15" fill="rgba(255,255,255,0.03)" stroke="rgba(255,255,255,0.1)"/>
              <text x="427.5" y="19" fill="#E2E8F0" text-anchor="middle">Figma</text>
            </g>
          </g>
        </g>

        <g transform="translate(0, 360)" fill="#94A3B8" opacity="0">
          <animate attributeName="opacity" values="0;1;1" keyTimes="0; 0.1; 1" begin="2.1s" dur="2s" fill="freeze" />
          
          <g transform="translate(0, 0)">
            <circle cx="15" cy="15" r="15" fill="rgba(255,255,255,0.05)" />
            <path d="M15 5.5c-5.25 0-9.5 4.25-9.5 9.5 0 4.2 2.72 7.76 6.5 9.02.48.09.65-.21.65-.46v-1.63c-2.64.57-3.2-1.28-3.2-1.28-.43-1.1-1.06-1.39-1.06-1.39-.86-.59.07-.58.07-.58.95.07 1.45.98 1.45.98.85 1.45 2.22 1.03 2.76.79.09-.61.33-1.03.6-1.27-2.11-.24-4.33-1.06-4.33-4.7 0-1.04.37-1.89.98-2.55-.1-.24-.43-1.21.09-2.52 0 0 .8-.26 2.62.98a9.12 9.12 0 0 1 2.38-.32c.81.01 1.62.11 2.38.32 1.82-1.24 2.62-.98 2.62-.98.52 1.31.2 2.28.1 2.52.61.66.98 1.51.98 2.55 0 3.65-2.23 4.45-4.35 4.69.34.29.64.87.64 1.75v2.6c0 .26.17.56.66.46C21.78 22.76 24.5 19.2 24.5 15c0-5.25-4.25-9.5-9.5-9.5z" fill="currentColor"/>
          </g>

          <g transform="translate(45, 0)">
            <circle cx="15" cy="15" r="15" fill="rgba(255,255,255,0.05)" />
            <path d="M8.8 22H5.5V10.7h3.3V22zM7.2 9.2c-1.1 0-1.9-.8-1.9-1.9s.8-1.9 1.9-1.9 1.9.8 1.9 1.9-.8 1.9-1.9 1.9zM24.5 22h-3.3v-5.5c0-1.3 0-3-1.8-3s-2.1 1.4-2.1 2.9V22h-3.3V10.7h3.2v1.5h.1c.4-.8 1.5-1.7 3.1-1.7 3.3 0 3.9 2.2 3.9 5v6.5z" fill="currentColor"/>
          </g>

          <g transform="translate(90, 0)">
            <circle cx="15" cy="15" r="15" fill="rgba(255,255,255,0.05)" />
            <path d="M18.8 6.5h2.5l-5.5 6.3 6.5 8.7h-5.1l-4-5.2-4.5 5.2H6.2l5.8-6.6-6.1-8.4h5.2l3.6 4.8 4.1-4.8zm-.9 13.5h1.4L11.5 8h-1.5l8.1 12z" fill="currentColor"/>
          </g>

          <g transform="translate(135, 0)">
            <circle cx="15" cy="15" r="15" fill="rgba(255,255,255,0.05)" />
            <path d="M12.6 15.4c-.6.6-1.5.6-2.1 0-.6-.6-.6-1.5 0-2.1l2.8-2.8c1.2-1.2 3.1-1.2 4.2 0 1.2 1.2 1.2 3.1 0 4.2l-1.4 1.4M17.4 14.6c.6-.6 1.5-.6 2.1 0 .6.6.6 1.5 0 2.1l-2.8 2.8c-1.2 1.2-3.1 1.2-4.2 0-1.2-1.2-1.2-3.1 0-4.2l1.4-1.4" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
          </g>
        </g>
      </g>
    </g>
  </g>
</svg>







# 💫 About Me:
Hey there! 👋 I'm Abhinand, a **passionate MERN Stack Developer** with a knack for **full-stack applications** and a special interest in **data structures**. I love solving complex **real-world problems** and building **responsive, dynamic applications** using **JavaScript, Node.js, Express, MongoDB, and React**. With a strong foundation in **data structures**, I aim to write clean, efficient code to optimize both performance and user experience. 🌐💡<br><br>### Ask me about:<br>- **Web Development** 🔧 – particularly with the MERN stack!<br>- **Data Structures & Algorithms** 📐 – from arrays and linked lists to trees and graphs, I enjoy diving deep into data organization and efficiency.<br>- **Database Design** 📊 – crafting optimized schemas is my jam.<br>- **Problem Solving** 🧩 – there's nothing better than tackling a tricky coding challenge!<br><br>## Fun Fact 🎉<br>I'm always on the lookout for new ways to make code **simpler and more efficient**, and I believe the right data structure can be a game-changer in any project!

<p align="left"> <img src="https://komarev.com/ghpvc/?username=abhinand-sd&label=Profile%20views&color=0e75b6&style=flat" alt="abhinand-sd" /> </p>

## 🌐 Socials:
[![Facebook](https://img.shields.io/badge/Facebook-%231877F2.svg?logo=Facebook&logoColor=white)]([https://www.facebook.com/me/](https://www.facebook.com/)) [![Instagram](https://img.shields.io/badge/Instagram-%23E4405F.svg?logo=Instagram&logoColor=white)](https://instagram.com/abhinand.sd_) [![LinkedIn](https://img.shields.io/badge/LinkedIn-%230077B5.svg?logo=linkedin&logoColor=white)](https://linkedin.com/in/abhinand-sd)  [![X](https://img.shields.io/badge/X-black.svg?logo=X&logoColor=white)](https://x.com/abhinand_sd_)

# 💻 Tech Stack:
![C++](https://img.shields.io/badge/c++-%2300599C.svg?style=plastic&logo=c%2B%2B&logoColor=white) ![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=plastic&logo=javascript&logoColor=%23F7DF1E) ![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=plastic&logo=html5&logoColor=white) ![TypeScript](https://img.shields.io/badge/typescript-%23007ACC.svg?style=plastic&logo=typescript&logoColor=white) ![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=plastic&logo=css3&logoColor=white) ![Google Cloud](https://img.shields.io/badge/GoogleCloud-%234285F4.svg?style=plastic&logo=google-cloud&logoColor=white) ![Cloudflare](https://img.shields.io/badge/Cloudflare-F38020?style=plastic&logo=Cloudflare&logoColor=white) ![Firebase](https://img.shields.io/badge/firebase-%23039BE5.svg?style=plastic&logo=firebase) ![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=plastic&logo=amazon-aws&logoColor=white) ![Bootstrap](https://img.shields.io/badge/bootstrap-%238511FA.svg?style=plastic&logo=bootstrap&logoColor=white) ![Chart.js](https://img.shields.io/badge/chart.js-F5788D.svg?style=plastic&logo=chart.js&logoColor=white) ![Express.js](https://img.shields.io/badge/express.js-%23404d59.svg?style=plastic&logo=express&logoColor=%2361DAFB) ![JWT](https://img.shields.io/badge/JWT-black?style=plastic&logo=JSON%20web%20tokens) ![jQuery](https://img.shields.io/badge/jquery-%230769AD.svg?style=plastic&logo=jquery&logoColor=white) ![NPM](https://img.shields.io/badge/NPM-%23CB3837.svg?style=plastic&logo=npm&logoColor=white) ![NodeJS](https://img.shields.io/badge/node.js-6DA55F?style=plastic&logo=node.js&logoColor=white) ![Next JS](https://img.shields.io/badge/Next-black?style=plastic&logo=next.js&logoColor=white) ![Pug](https://img.shields.io/badge/Pug-FFF?style=plastic&logo=pug&logoColor=A86454) ![Socket.io](https://img.shields.io/badge/Socket.io-black?style=plastic&logo=socket.io&badgeColor=010101) ![Redux](https://img.shields.io/badge/redux-%23593d88.svg?style=plastic&logo=redux&logoColor=white) ![React](https://img.shields.io/badge/react-%2320232a.svg?style=plastic&logo=react&logoColor=%2361DAFB) ![React Query](https://img.shields.io/badge/-React%20Query-FF4154?style=plastic&logo=react%20query&logoColor=white) ![TailwindCSS](https://img.shields.io/badge/tailwindcss-%2338B2AC.svg?style=plastic&logo=tailwind-css&logoColor=white) ![Yarn](https://img.shields.io/badge/yarn-%232C8EBB.svg?style=plastic&logo=yarn&logoColor=white) ![Nginx](https://img.shields.io/badge/nginx-%23009639.svg?style=plastic&logo=nginx&logoColor=white) ![Firebase](https://img.shields.io/badge/firebase-a08021?style=plastic&logo=firebase&logoColor=ffcd34) ![MongoDB](https://img.shields.io/badge/MongoDB-%234ea94b.svg?style=plastic&logo=mongodb&logoColor=white) ![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=plastic&logo=postgresql&logoColor=white) ![Adobe](https://img.shields.io/badge/adobe-%23FF0000.svg?style=plastic&logo=adobe&logoColor=white) ![Figma](https://img.shields.io/badge/figma-%23F24E1E.svg?style=plastic&logo=figma&logoColor=white) ![Canva](https://img.shields.io/badge/Canva-%2300C4CC.svg?style=plastic&logo=Canva&logoColor=white) ![Git](https://img.shields.io/badge/git-%23F05033.svg?style=plastic&logo=git&logoColor=white) ![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=plastic&logo=github&logoColor=white) ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=plastic&logo=docker&logoColor=white) ![Postman](https://img.shields.io/badge/Postman-FF6C37?style=plastic&logo=postman&logoColor=white)
[![](https://visitcount.itsvg.in/api?id=abhinand-sd&icon=8&color=1)](https://visitcount.itsvg.in)

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f0c29,50:302b63,100:24243e&height=140&section=header&text=&animation=fadeIn" width="100%"/>

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=700&size=32&duration=2800&pause=1200&color=A78BFA&center=true&vCenter=true&width=960&lines=Mr+Abhinand+SD;AI+%26+Full+Stack+Developer;AWS+Certified+AI+Practitioner;Competitive+Programmer+%7C+Tech+Fellow" alt="Typing SVG" />

<br/>

<p>
  <img src="https://img.shields.io/badge/B.Tech_AIML-Aditya_Engineering_College-7C3AED?style=flat-square&logo=graduation-cap&logoColor=white"/>
  &nbsp;
  <img src="https://img.shields.io/badge/CGPA-9.10_/_10-10B981?style=flat-square"/>
  &nbsp;
  <img src="https://img.shields.io/badge/Location-Andhra_Pradesh,_India-6366F1?style=flat-square&logo=googlemaps&logoColor=white"/>
</p>

<p>
  <a href="https://videoportfolio-kohl.vercel.app/" target="_blank">
    <img src="https://img.shields.io/badge/Portfolio-Live-A78BFA?style=for-the-badge&logo=vercel&logoColor=white"/>
  </a>
  &nbsp;
  <a href="https://www.linkedin.com/in/abhinand-sd/" target="_blank">
    <img src="https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white"/>
  </a>
  &nbsp;
  <a href="mailto:abhinandsd49@gmail.com">
    <img src="https://img.shields.io/badge/Email-Reach_Out-EA4335?style=for-the-badge&logo=gmail&logoColor=white"/>
  </a>
  &nbsp;
  <a href="https://github.com/abhinand-sd" target="_blank">
    <img src="https://img.shields.io/badge/GitHub-Follow-181717?style=for-the-badge&logo=github&logoColor=white"/>
  </a>
</p>

<img src="https://komarev.com/ghpvc/?username=Sushmitadasari&color=7C3AED&style=flat-square&label=Profile+Views"/>
&nbsp;
<img src="https://img.shields.io/github/followers/abhinand-sd?style=flat-square&color=6366F1&label=Followers"/>
&nbsp;
<img src="https://img.shields.io/github/stars/abhinand-sd?style=flat-square&color=A78BFA&label=Stars"/>

</div>

<br/>

---

## About

I am an **AI & Machine Learning engineer** and **Full Stack Developer** with a strong foundation in building production-grade intelligent systems. Currently pursuing B.Tech in AIML at Aditya Engineering College, where I hold the position of **Branch Topper** with a 9.10 CGPA.

My engineering work spans the full lifecycle — from training and fine-tuning language models to deploying scalable multi-tenant SaaS infrastructure. I have shipped systems that process hundreds of documents, handle thousands of financial transactions, and support enterprise-grade access control — all built from the ground up.

I combine the rigor of competitive programming (650+ problems across LeetCode, GFG, CodeChef) with the product thinking required to build tools that real users rely on.

**Open to:** Software Engineering Internships · AI/ML Engineer Roles · Full Stack Developer Roles

---

## Tech Stack

### Languages

<p>
  <img src="https://skillicons.dev/icons?i=java,python,cpp,c,javascript&theme=dark"/>
</p>

### Frontend

<p>
  <img src="https://skillicons.dev/icons?i=react,html,css,js&theme=dark"/>
</p>

### Backend & Databases

<p>
  <img src="https://skillicons.dev/icons?i=nodejs,express,postgres,mongodb,mysql&theme=dark"/>
</p>

### Cloud, DevOps & Tooling

<p>
  <img src="https://skillicons.dev/icons?i=aws,docker,git,github,postman&theme=dark"/>
</p>

---

## AI / ML Expertise

| Domain | Proficiency | Details |
|---|---|---|
| **Large Language Models** | Advanced | Prompt engineering, RAG pipelines, LLM API integration |
| **Natural Language Processing** | Expert | Document parsing, text classification, entity extraction |
| **Machine Learning** | Advanced | Supervised/unsupervised learning, model evaluation |
| **Document AI** | Experienced | Policy analysis, structured extraction from unstructured data |
| **AWS AI Services** | Certified | AI Practitioner · Cloud Foundations |
| **Deep Learning** | Intermediate | Neural networks, NPTEL certified |

---

## Featured Projects

<details>
<summary><b>PolicyGuard AI — AI-Powered Policy Intelligence Platform</b></summary>

<br/>

> Intelligent policy analysis platform delivering real-time insights across web, mobile, browser extension, and desktop surfaces.

| Attribute | Detail |
|---|---|
| **Stack** | Python · NLP · LLM · REST APIs |
| **Scale** | 500+ policy documents processed |
| **Accuracy** | 92% analysis accuracy |
| **Impact** | 60% reduction in manual review time |
| **Delivery** | Web · Mobile · Browser Extension · Desktop |
| **Repository** | [github.com/abhinand-sd/PolicyGuard-AI](https://github.com/abhinand-sd/PolicyGuard-AI) |

**What it does:** Parses and interprets complex policy documents at scale using LLMs and NLP pipelines. Surfaces structured policy insights in real time across multiple client platforms, eliminating hours of manual legal and compliance review.

</details>

<details>
<summary><b>Payment Gateway System — Full Stack Payment Infrastructure</b></summary>

<br/>

> Production-grade payment processing infrastructure with Dockerized microservices and sub-100ms API response times.

| Attribute | Detail |
|---|---|
| **Stack** | React · Node.js · Express · PostgreSQL · Docker |
| **Scale** | 1,000+ transactions processed |
| **Uptime** | 99.8% system availability |
| **Performance** | 40% reduction in API response time |
| **Architecture** | Dockerized microservices |
| **Repository** | [github.com/abhinand-sd/Payment-gateway-system-Project](https://github.com/abhinand-sd/Payment-gateway-system-Project) |

**What it does:** End-to-end payment system with secure transaction handling, idempotency guarantees, and containerized deployment. Built with a focus on reliability, auditability, and horizontal scalability.

</details>

<details>
<summary><b>Multi-Tenant SaaS Platform — Enterprise Architecture</b></summary>

<br/>

> Enterprise SaaS backbone supporting concurrent tenants with role-based access control and one-click deployment.

| Attribute | Detail |
|---|---|
| **Stack** | Node.js · React · PostgreSQL · Docker Compose |
| **Scale** | 50+ concurrent tenants |
| **Security** | JWT authentication · RBAC authorization |
| **Operations** | One-click deployment pipeline |
| **Record** | Zero unauthorized access incidents |
| **Repository** | [github.com/abhinand-sd/Multi-Tenant-SaaS-Platform](https://github.com/abhinand-sd/Multi-Tenant-SaaS-Platform) |

**What it does:** Full multi-tenancy infrastructure with strict data isolation between tenants, row-level security, and centralized identity management. Designed for startup-to-enterprise scale with minimal operational overhead.

</details>

<details>
<summary><b>Video Portfolio — Personal Branding Platform</b></summary>

<br/>

> Modern, recruiter-optimized developer portfolio with video introduction and mobile-first responsive design.

| Attribute | Detail |
|---|---|
| **Stack** | React · Vercel |
| **Live URL** | [videoportfolio-kohl.vercel.app](https://videoportfolio-kohl.vercel.app/) |
| **Features** | Video intro · Mobile responsive · Premium UI/UX |

</details>

---

## Experience

### Full Stack Development Trainee — Technical Hub Pvt Ltd

`May 2025 – June 2026`

Embedded within a software engineering team building and maintaining production web applications. Contributed across the full development lifecycle — from UI implementation to database design, API development, and containerized deployment.

**Scope of work:**
- Built React frontends and Node.js/Express backends for client-facing applications
- Designed and integrated relational databases (PostgreSQL) and REST APIs
- Deployed applications using Docker with Git-based CI/CD workflows
- Participated in debugging, performance profiling, and code reviews

`React` `Node.js` `PostgreSQL` `Docker` `REST APIs` `Git`

---

## Achievements

<div align="center">

| Recognition | Details |
|---|---|
| Flipkart GRiD 7.0 | Semi-Finalist — National-level engineering competition |
| AlgoUniversity Tech Fellow | Competitive selection — merit-based program |
| AIML Branch Topper | 9.24 SGPA — Highest in department |
| LeetCode | 350+ problems solved |
| GeeksforGeeks | 300+ problems solved |
| HackerRank | 5-Star in Java, Python, C, and SQL |
| CodeChef | 200+ problems solved |

</div>

---

## Certifications

<div align="center">

**Amazon Web Services**

![AWS AI Practitioner](https://img.shields.io/badge/AWS-AI_Practitioner-FF9900?style=flat-square&logo=amazonaws&logoColor=white)
&nbsp;
![AWS Cloud Foundations](https://img.shields.io/badge/AWS-Cloud_Foundations-232F3E?style=flat-square&logo=amazonaws&logoColor=white)

<br/>

**Oracle**

![Oracle Java](https://img.shields.io/badge/Oracle-Java_Foundations-F80000?style=flat-square&logo=oracle&logoColor=white)
&nbsp;
![Oracle DB](https://img.shields.io/badge/Oracle-Database_Foundations-F80000?style=flat-square&logo=oracle&logoColor=white)

<br/>

**NPTEL**

![NPTEL DBMS](https://img.shields.io/badge/NPTEL-Database_Management_Systems-0F9D58?style=flat-square)
&nbsp;
![NPTEL AI](https://img.shields.io/badge/NPTEL-Artificial_Intelligence-4285F4?style=flat-square)
&nbsp;
![NPTEL DL](https://img.shields.io/badge/NPTEL-Deep_Learning-7B2FBE?style=flat-square)

<br/>

**Cisco Networking Academy**

![Cisco HTML](https://img.shields.io/badge/Cisco-HTML-1BA0D7?style=flat-square&logo=cisco&logoColor=white)
&nbsp;
![Cisco CSS](https://img.shields.io/badge/Cisco-CSS-1BA0D7?style=flat-square&logo=cisco&logoColor=white)
&nbsp;
![Cisco JS](https://img.shields.io/badge/Cisco-JavaScript-1BA0D7?style=flat-square&logo=cisco&logoColor=white)
&nbsp;
![Cisco Python](https://img.shields.io/badge/Cisco-Python-1BA0D7?style=flat-square&logo=cisco&logoColor=white)

</div>

---

## Coding Profiles

<div align="center">

<a href="https://leetcode.com/u/sushmita_dasari/" target="_blank">
  <img src="https://img.shields.io/badge/LeetCode-350+_Problems-FFA116?style=for-the-badge&logo=leetcode&logoColor=black"/>
</a>
&nbsp;
<a href="https://geeksforgeeks.org/user/sushmitadasari333/" target="_blank">
  <img src="https://img.shields.io/badge/GeeksforGeeks-300+_Problems-2F8D46?style=for-the-badge&logo=geeksforgeeks&logoColor=white"/>
</a>
&nbsp;
<a href="https://hackerrank.com/profile/sushmitadasari17" target="_blank">
  <img src="https://img.shields.io/badge/HackerRank-5★_Rated-00EA64?style=for-the-badge&logo=hackerrank&logoColor=black"/>
</a>
&nbsp;
<a href="https://codechef.com/users/sushmita173" target="_blank">
  <img src="https://img.shields.io/badge/CodeChef-200+_Problems-5B4638?style=for-the-badge&logo=codechef&logoColor=white"/>
</a>

</div>

---

## GitHub Analytics

<div align="center">

<img height="175" src="https://github-readme-stats.vercel.app/api?username=Sushmitadasari&show_icons=true&theme=tokyonight&border_radius=10&hide_border=false&include_all_commits=true&count_private=true" />
&nbsp;
<img height="175" src="https://github-readme-streak-stats.herokuapp.com/?user=Sushmitadasari&theme=tokyonight&border_radius=10&hide_border=false" />

<br/><br/>

<img height="175" src="https://github-readme-stats.vercel.app/api/top-langs/?username=Sushmitadasari&layout=compact&theme=tokyonight&border_radius=10&hide_border=false&langs_count=8" />

</div>

---

## GitHub Trophies

<div align="center">

<img src="https://github-profile-trophy.vercel.app/?username=Sushmitadasari&theme=tokyonight&no-frame=true&margin-w=12&row=2&column=4"/>

</div>

---

## Contribution Activity

<div align="center">

<img src="https://github-readme-activity-graph.vercel.app/graph?username=Sushmitadasari&theme=tokyo-night&hide_border=true&area=true" width="100%"/>

</div>

<div align="center">

<img src="https://raw.githubusercontent.com/Platane/snk/output/github-contribution-grid-snake-dark.svg" width="100%"/>

</div>

---

## Current Focus

```yaml
Learning:
  - System Design & Distributed Systems
  - Advanced Backend Architecture
  - Cloud Engineering on AWS

Building:
  - AI-powered production applications
  - SaaS platforms with enterprise-grade architecture
  - Developer tooling and branding products

Exploring:
  - Large Language Models & retrieval-augmented generation
  - Scalable event-driven systems
  - AWS ecosystem (ECS, Lambda, RDS, Bedrock)

Open To:
  - Software Engineering roles at product-first companies
  - AI / ML Engineer opportunities
  - Open source collaborations
```

---

## Connect

<div align="center">

<a href="mailto:sushmitadasari17@gmail.com">
  <img src="https://img.shields.io/badge/Gmail-sushmitadasari17@gmail.com-EA4335?style=for-the-badge&logo=gmail&logoColor=white"/>
</a>
&nbsp;
<a href="https://www.linkedin.com/in/sushmita-dasari-227a40284/" target="_blank">
  <img src="https://img.shields.io/badge/LinkedIn-Sri_Sushmita_Dasari-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white"/>
</a>
&nbsp;
<a href="https://github.com/Sushmitadasari" target="_blank">
  <img src="https://img.shields.io/badge/GitHub-Sushmitadasari-181717?style=for-the-badge&logo=github&logoColor=white"/>
</a>
&nbsp;
<a href="https://videoportfolio-kohl.vercel.app/" target="_blank">
  <img src="https://img.shields.io/badge/Portfolio-Live_Website-7C3AED?style=for-the-badge&logo=vercel&logoColor=white"/>
</a>

</div>

<br/>

<div align="center">

*Building at the intersection of AI, full-stack engineering, and systems thinking.*

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:24243e,50:302b63,100:0f0c29&height=120&section=footer" width="100%"/>

</div>
