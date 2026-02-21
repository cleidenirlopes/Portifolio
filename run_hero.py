import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

start_marker = r'<!--==============================  HOME SECTION ==============================-->'
end_marker = r'<!--============================== SKILL SECTION ==============================-->'

new_html = """<!--==============================  HOME SECTION ==============================-->
	</head>

	<body class="home" style="background-color: #121212; color: #e0e0e0; margin: 0; padding: 0;">

		<!-- Command Center Executive Summary -->
		<header id="header" style="max-width: 1200px; margin: 100px auto 60px auto; padding: 0 20px;">
			<div class="executive-dashboard-card" style="background-color: #1A2238; border-radius: 16px; box-shadow: 0 10px 30px rgba(0, 0, 0, 0.6); display: flex; flex-wrap: wrap; overflow: hidden; border: 1px solid rgba(255,255,255,0.05);">
				
				<!-- Left Profile Info -->
				<div style="flex: 1; min-width: 320px; padding: 50px 40px; display: flex; flex-direction: column; justify-content: center; border-right: 1px solid rgba(255,255,255,0.05);">
					<h1 id="logo" style="margin-bottom: 5px;">
						<!-- Name and Logo -->
						<span style="font-size: 42px; font-weight: 700; color: #ffffff; letter-spacing: -1px;">Cledenir</span>
						<img width="50px" style="vertical-align: text-bottom; margin: 0 5px;" src="assets/images/logo.webp" alt="Logo">
						<span style="font-size: 42px; font-weight: 700; color: #ffffff; letter-spacing: -1px;">Souza</span>
					</h1>
					<h2 style="font-size: 20px; color: #2b88c6; margin-bottom: 25px; font-weight: 600;">Data Analyst & Visualizer</h2>

					<p style="color: #e0e0e0; font-size: 16px; line-height: 1.7; margin-bottom: 25px;">
						👋 Hi! I am passionate about transforming raw data into meaningful insights. With over 8 years of experience in technical support and a background in Computer Science, I bring robust problem-solving skills to data analytics.
					</p>

					<!-- Social Media Links -->
					<div class="social-links" style="display: flex; gap: 20px; margin-bottom: 30px;">
						<a href="https://github.com/cleidenirlopes" target="_blank" style="font-size: 24px; color: #b0b0b0; transition: color 0.3s ease;" onmouseover="this.style.color='#2b88c6'" onmouseout="this.style.color='#b0b0b0'"><i class="fab fa-github"></i></a>
						<a href="https://www.linkedin.com/in/cledenir-souza-01a920162/" target="_blank" style="font-size: 24px; color: #b0b0b0; transition: color 0.3s ease;" onmouseover="this.style.color='#2b88c6'" onmouseout="this.style.color='#b0b0b0'"><i class="fab fa-linkedin"></i></a>
						<a href="https://x.com/DCledenir" target="_blank" style="font-size: 24px; color: #b0b0b0; transition: color 0.3s ease;" onmouseover="this.style.color='#2b88c6'" onmouseout="this.style.color='#b0b0b0'"><i class="fab fa-twitter"></i></a>
					</div>

					<button onclick="window.location.href = 'contact-me.html';" style="background-color: #2b88c6; color: #ffffff; border: none; padding: 12px 28px; font-size: 15px; border-radius: 6px; cursor: pointer; transition: background-color 0.3s ease; width: fit-content; font-weight: 600; box-shadow: 0 4px 12px rgba(43, 136, 198, 0.3);" onmouseover="this.style.backgroundColor='#1f689e'" onmouseout="this.style.backgroundColor='#2b88c6'">
						Contact Me
					</button>
				</div>

				<!-- Middle About Details -->
				<div style="flex: 1.5; min-width: 320px; padding: 50px 40px; display: flex; flex-direction: column; justify-content: center;">
					<h3 style="color: #ffffff; font-size: 22px; margin-bottom: 20px; border-bottom: 2px solid #2b88c6; padding-bottom: 10px; display: inline-block;">Executive Summary</h3>
					
					<p style="font-size: 15px; color: #b0b0b0; line-height: 1.8; margin-bottom: 15px;">
						<strong style="color: #e0e0e0;">Background:</strong> I've always had a passion for technology, which led me to pursue a degree in Computer Science. I worked for over 10 years as a Technical Support Specialist, gaining extensive experience in solving complex technical issues.
					</p>
					
					<p style="font-size: 15px; color: #b0b0b0; line-height: 1.8; margin-bottom: 15px;">
						<strong style="color: #e0e0e0;">Creative Edge:</strong> Later, I transitioned into Graphic Design, an area I truly love that has become more than just a job—it's a fulfilling hobby that informs my dashboard design.
					</p>

					<p style="font-size: 15px; color: #b0b0b0; line-height: 1.8; margin-bottom: 15px;">
						<strong style="color: #e0e0e0;">Current Focus:</strong> For the past year, I've been diving into the world of Data Analysis, and I'm currently finishing a Data Analytics Bootcamp to strengthen my skills.
					</p>

					<p style="font-size: 15px; color: #b0b0b0; line-height: 1.8; margin-bottom: 0;">
						<strong style="color: #e0e0e0;">Objective:</strong> My goal is to become a Data Visualization professional, combining my technical background and creative skills to transform data into meaningful insights and impactful stories.
					</p>
				</div>

				<!-- Right Media View -->
				<div style="flex: 0.8; min-width: 250px; background-color: #121212; display: flex; align-items: center; justify-content: center; position: relative; overflow: hidden;">
					<div style="position: absolute; top:0; left:0; width: 100%; height: 100%; background: linear-gradient(to right, #1A2238 0%, transparent 20%); z-index: 1;"></div>
					<!-- Image Right Rule preserved: Profile on right -->
					<img src="assets/images/Profile.JPG" alt="Profile Image" style="width: 100%; height: 100%; object-fit: cover; opacity: 0.85;">
				</div>
			</div>
		</header>

"""

pattern = start_marker + r'.*?' + end_marker
new_text = re.sub(pattern, new_html + end_marker, text, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_text)

print("Replacement successful")
