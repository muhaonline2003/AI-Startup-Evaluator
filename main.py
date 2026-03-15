

import streamlit as st
import backend_api
from typing import Any, Dict, List
import PyPDF2

st.set_page_config(
	page_title="Startup Ecosystem Platform",
	page_icon="🚀",
	layout="wide"
)
## Removed Streamlit logo from sidebar
st.sidebar.title("🌌 Ecosystem OS")
st.sidebar.caption("Role-based startup ecosystem dashboard.")

# --- Classic dark theme injection ---
def inject_dark_theme():
	st.markdown(
		"""
		<style>
		body, .stApp, .css-18e3th9, .css-1d391kg, .css-1v0mbdj, .css-1dp5vir, .css-1cpxqw2 {
			background: #0f172a !important;
			color: #e5e7eb !important;
		}
		.stSidebar, .css-6qob1r, .css-1lcbmhc {
			background: #181f2a !important;
		}
		.stButton>button, .stTextInput>div>input, .stSelectbox>div>div>div>input, .stTextArea>div>textarea {
			background: #1e293b !important;
			color: #e5e7eb !important;
			border: 1px solid #334155 !important;
		}
		.stRadio>div>label {
			color: #e5e7eb !important;
		}
		.stDataFrame, .stDataFrame table {
			background: #181f2a !important;
			color: #e5e7eb !important;
		}
		</style>
		""",
		unsafe_allow_html=True,
	)
inject_dark_theme()

# =============================================================
# Streamlit Frontend for Startup Ecosystem Dashboard
# -------------------------------------------------------------
# - All business logic, CRUD, and AI is handled by the FastAPI backend
# - This frontend communicates with the backend via backend_api.py
# - Only UI rendering and API calls are done here
# =============================================================

# =============================================================
# Streamlit Frontend for Startup Ecosystem Dashboard
# -------------------------------------------------------------
# - All business logic, CRUD, and AI is handled by the FastAPI backend
# - This frontend communicates with the backend via backend_api.py
# - Only UI rendering and API calls are done here
# =============================================================
st.sidebar.markdown("---")
st.sidebar.markdown("**Storage**: JSON files (startups.json, investors.json, developers.json, events.json, networking.json)")
st.sidebar.caption("For production, upgrade to SQLite/PostgreSQL.")
import streamlit as st
import backend_api
from typing import Any, Dict, List
import PyPDF2

# Role-based navigation: each role sees a tailored set of sections
ROLE_SECTIONS = {
	"Founder": [
		"Dashboard",
		"My Startup",
		"AI Assistant",
		"Networking",
		"Events",
	],
	"Investor": [
		"Dashboard",
		"Startup Directory",
		"Shortlist",
		"Deal Flow",
		"AI Assistant",
		"Events",
	],
	"Developer": [
		"Dashboard",
		"My Profile",
		"Opportunities",
		"Networking",
		"AI Assistant",
		"Events",
	],
	"Accelerator": [
		"Dashboard",
		"Startups",
		"Investors",
		"Developers",
		"Deal Flow",
		"Events",
		"AI Assistant",
	],
}

role = st.sidebar.selectbox(
	"Active role",
	list(ROLE_SECTIONS.keys()),
)

available_sections = ROLE_SECTIONS.get(role, ROLE_SECTIONS["Accelerator"])
section = st.sidebar.radio("Section", available_sections)


# Load data from backend API (all CRUD and AI now via backend)
startups = backend_api.get_startups()
networking_posts = backend_api.get_networking()
investors = backend_api.get_investors()
developers = backend_api.get_developers()
events = backend_api.get_events()


def compute_kpis(startups_list: List[Dict[str, Any]], posts: List[Dict[str, Any]]) -> Dict[str, Any]:
	"""Compute simple KPIs for the global dashboard using real counts where possible."""
	active_startups = len(startups_list)
	try:
		active_investors = len(investors)
	except Exception:
		active_investors = max(1, int(active_startups * 0.3))
	deal_pipeline = int(active_startups * 1.5)
	try:
		upcoming_events = len(events)
	except Exception:
		upcoming_events = 0
	return {
		"active_startups": active_startups,
		"active_investors": active_investors,
		"deal_pipeline": deal_pipeline,
		"upcoming_events": upcoming_events,
	}


def render_hero(role_label: str) -> None:
	"""Top hero block with premium gradient, icon, and accent badge."""
	subtitle_map = {
		"Founder": "Submit your startup, get AI feedback, and discover connections.",
		"Investor": "Discover, evaluate, and track high-signal startup opportunities.",
		"Developer": "Find teams that need builders and technical cofounders.",
		"Accelerator": "Monitor your portfolio and pipeline in one place.",
	}
	icon_map = {
		"Founder": "🚀",
		"Investor": "💸",
		"Developer": "💻",
		"Accelerator": "🌐",
	}
	st.markdown(
		f"""
		<div style="margin-bottom: 12px; border-radius: 28px; background: linear-gradient(90deg,#6366f1 0%,#0ea5e9 100%); box-shadow: 0 8px 32px #0ea5e9; padding: 2.5rem 2.2rem 1.7rem 2.2rem; display:flex; align-items:center; justify-content:space-between;">
		  <div style="display:flex; align-items:center; gap:18px;">
		    <div class="icon-badge" style="font-size:2.1rem;">{icon_map.get(role_label,"🌐")}</div>
		    <div>
		      <div class="badge" style="margin-bottom:6px;">Active role · {role_label}</div>
		      <h1 style="margin: 0 0 2px 0; font-size: 2.1rem; font-weight:800; color:#fff; text-shadow:0 2px 12px #0ea5e9;">Startup Ecosystem Platform</h1>
		      <p style="margin: 0; font-size: 1.08rem; color: #bae6fd; font-weight:500;">{subtitle_map.get(role_label, "Role-based startup operating system.")}</p>
		    </div>
		  </div>
		  <div style="text-align:right; font-size:1.02rem; color:#fff;">
		    <div class="icon-badge" style="background:linear-gradient(90deg,#a5b4fc 0,#38bdf8 100%); color:#312e81; font-size:1.1rem; margin-bottom:6px;">✨ Premium Demo</div>
		    <div style="margin-top:2px; opacity:0.92;">Powered by OpenAI</div>
		    <div style="margin-top:2px; opacity:0.85; font-size:0.95rem;">AI Startup Evaluator MVP</div>
		  </div>
		</div>
		""",
		unsafe_allow_html=True,
	)


def render_kpi_row() -> None:
	"""Render top KPI metric cards with colorful icons and gradients."""
	kpis = compute_kpis(startups, networking_posts)
	icon_map = [
		"<span style='font-size:2.1rem;'>🚀</span>",
		"<span style='font-size:2.1rem;'>💸</span>",
		"<span style='font-size:2.1rem;'>📈</span>",
		"<span style='font-size:2.1rem;'>📅</span>"
	]
	labels = ["Active startups", "Active investors", "Deals in pipeline", "Upcoming events"]
	values = [kpis['active_startups'], kpis['active_investors'], kpis['deal_pipeline'], kpis['upcoming_events']]
	pills = ["Portfolio", "Capital side", "Pipeline", "Ecosystem"]
	st.markdown('<div class="kpi-row" style="margin-bottom: 1.5rem;">', unsafe_allow_html=True)
	cols = st.columns(4)
	for i in range(4):
		with cols[i]:
			st.markdown(
				f"""
				<div style="background: rgba(16,23,42,0.85); border: 2px solid #38bdf8; box-shadow: 0 4px 24px #0ea5e922; border-radius: 18px; padding: 1.3rem 1.1rem 1.1rem 1.1rem; margin-bottom: 0.5rem; min-height: 120px; display: flex; flex-direction: column; justify-content: space-between;">
				  <div style='display:flex;align-items:center;gap:12px;'>
					{icon_map[i]}
					<div>
					  <div style='font-size:1.08rem; font-weight:600; color:#fff; margin-bottom:2px;'>{labels[i]}</div>
					  <div style='font-size:2.1rem; font-weight:800; color:#fff; text-shadow:0 2px 12px #0ea5e9;'>{values[i]}</div>
					</div>
				  </div>
				  <div style='margin-top:10px; font-size:0.98rem; color:#bae6fd; font-weight:500;'>{pills[i]}</div>
				</div>
				""",
				unsafe_allow_html=True,
			)
	st.markdown('</div>', unsafe_allow_html=True)


def render_startup_profile_card(startup: Dict[str, Any]) -> None:
	"""Nicely formatted startup profile card using existing fields and AI analysis."""
	analysis = startup.get("analysis", {}) or {}
	score = analysis.get("score", "N/A")
	readiness = analysis.get("investor_readiness", "")
	badge_class = "badge"
	if isinstance(score, (int, float)) or (isinstance(score, str) and score.replace(".", "", 1).isdigit()):
		try:
			s_val = float(score)
		except Exception:
			s_val = -1
		if s_val >= 8:
			badge_class = "badge badge-success"
		elif s_val >= 6:
			badge_class = "badge badge-warn"
		else:
			badge_class = "badge badge-risk"

	st.markdown(
		f"""
		<div class="card-subtle" style="margin-top:8px;">
		  <div style="display:flex; justify-content: space-between; align-items:flex-start; gap: 12px;">
		    <div>
		      <div style="font-size:0.75rem; text-transform:uppercase; letter-spacing:.08em; color:#6b7280; margin-bottom:2px;">Startup</div>
		      <div style="display:flex; align-items:center; gap:6px;">
		        <h3 style="margin:0 0 2px 0; font-size:1.0rem;">{startup.get('name','')}</h3>
		      </div>
		      <p style="margin:0; font-size:0.78rem; color:#9ca3af;">{startup.get('industry','')} · {startup.get('stage','')}</p>
		      <p style="margin:4px 0 0 0; font-size:0.76rem; color:#d1d5db;">Founder: {startup.get('founder','')}</p>
		    </div>
		    <div style="text-align:right; min-width:120px;">
		      <div class="{badge_class}">AI Score: {score}</div>
		      <div style="margin-top:6px; font-size:0.7rem; color:#9ca3af; max-width:170px;">{readiness}</div>
		    </div>
		  </div>
		  <div style="margin-top:10px; font-size:0.78rem; color:#d1d5db; display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:10px;">
		    <div><div style="font-size:0.72rem; color:#6b7280;">Problem</div><div>{startup.get('problem','')}</div></div>
		    <div><div style="font-size:0.72rem; color:#6b7280;">Solution</div><div>{startup.get('solution','')}</div></div>
		    <div><div style="font-size:0.72rem; color:#6b7280;">Target market</div><div>{startup.get('target_market','')}</div></div>
		  </div>
		</div>
		""",
		unsafe_allow_html=True,
	)


def render_founder_workspace() -> None:
	"""Founder-focused workspace: submit startup + view AI analysis."""
	st.markdown("##### Founder workspace · Submit & evaluate your startup")
	with st.form("startup_form"):
		col1, col2 = st.columns(2)
		with col1:
			name = st.text_input("Startup Name")
			founder = st.text_input("Founder Name")
			industry = st.text_input("Industry / Sector")
			stage = st.selectbox(
				"Stage",
				["Idea", "MVP", "Pre-seed", "Seed", "Series A+"],
				index=1,
			)
		with col2:
			problem = st.text_area("Problem", height=80)
			solution = st.text_area("Solution", height=80)
			target_market = st.text_area("Target Market", height=80)

		st.markdown("---")
		st.markdown("**Pitch input**")
		pitch_input_mode = st.radio(
			"How do you want to provide the pitch?",
			["Paste text", "Upload PDF"],
		)

		pitch_text = ""
		uploaded_file = None
		if pitch_input_mode == "Paste text":
			pitch_text = st.text_area("Paste your pitch text", height=160)
		else:
			uploaded_file = st.file_uploader("Upload pitch deck PDF", type=["pdf"])

		submitted = st.form_submit_button("Run AI Evaluation")

	if submitted:
		if not name or not industry or not stage:
			st.warning("Please fill at least Startup Name, Industry and Stage.")
		else:
			if pitch_input_mode == "Upload PDF":
				if not uploaded_file:
					st.warning("Please upload a PDF or switch to text mode.")
					st.stop()
				pitch_text_val = extract_text_from_pdf(uploaded_file)
				if not pitch_text_val:
					st.warning("Could not extract text from PDF. Try pasting the pitch text instead.")
					st.stop()
			else:
				if not pitch_text.strip():
					st.warning("Please paste your pitch text.")
					st.stop()
				pitch_text_val = pitch_text

			startup = {
				"name": name.strip(),
				"founder": founder.strip(),
				"industry": industry.strip(),
				"stage": stage,
				"problem": problem.strip(),
				"solution": solution.strip(),
				"target_market": target_market.strip(),
				"pitch_text": pitch_text_val.strip(),
			}

			with st.spinner("Analyzing startup pitch with AI..."):
				analysis = backend_api.ai_evaluate_startup(startup)

			startup["analysis"] = analysis
			startups = backend_api.create_startup(startup)
			st.success("Analysis complete and startup saved to JSON.")

			col_left, col_right = st.columns([2, 1])
			with col_left:
				st.markdown("###### Startup profile")
				render_startup_profile_card(startup)
			with col_right:
				st.markdown("###### AI score")
				score_value = analysis.get("score", "N/A")
				st.metric("Overall Score /10", str(score_value))
				st.write("**Investor readiness:**")
				st.write(analysis.get("investor_readiness", ""))

			st.markdown("---")
			st.markdown("###### AI evaluation breakdown")
			col_b1, col_b2 = st.columns(2)
			with col_b1:
				st.write("**Problem clarity:**", analysis.get("problem_clarity", ""))
				st.write("**Solution strength:**", analysis.get("solution_strength", ""))
				st.write("**Market potential:**", analysis.get("market_potential", ""))
			with col_b2:
				st.write("**Business model clarity:**", analysis.get("business_model", ""))
				st.write("**Investor recommendation:**", analysis.get("investor_recommendation", ""))

			summary = analysis.get("summary", "")
			if summary:
				st.markdown("**Summary**")
				st.info(summary)

			strengths = analysis.get("strengths", []) or []
			weaknesses = analysis.get("weaknesses", []) or []
			risks = analysis.get("risks", []) or []
			suggestions = analysis.get("suggestions", []) or []

			cols_lists = st.columns(3)
			with cols_lists[0]:
				if strengths:
					st.markdown("**Strengths**")
					for item in strengths:
						st.write(f"- {item}")
			with cols_lists[1]:
				if weaknesses:
					st.markdown("**Weaknesses**")
					for item in weaknesses:
						st.write(f"- {item}")
			with cols_lists[2]:
				if risks:
					st.markdown("**Risks**")
					for item in risks:
						st.write(f"- {item}")

			if suggestions:
				st.markdown("**Suggestions for improvement**")
				for item in suggestions:
					st.write(f"- {item}")


def render_directory_table(shortlist_enabled: bool = False) -> None:
	"""Investor-focused directory view with filters and expanders."""
	if not startups:
		st.info("No startups submitted yet. Use the Founder workspace to add one.")
		return

	industries = sorted({s.get("industry", "") for s in startups if s.get("industry")})
	stages = sorted({s.get("stage", "") for s in startups if s.get("stage")})

	col_f1, col_f2, col_f3 = st.columns(3)
	with col_f1:
		selected_industries = st.multiselect("Industry", industries, default=industries)
	with col_f2:
		selected_stages = st.multiselect("Stage", stages, default=stages)
	with col_f3:
		min_score = st.slider("Minimum score", 0.0, 10.0, 0.0, 0.5)

	filtered = []
	scores_numeric: List[float] = []
	for s in startups:
		analysis = s.get("analysis", {}) or {}
		score = analysis.get("score")
		try:
			score_num = float(score)
		except Exception:
			score_num = None

		if industries and s.get("industry") not in selected_industries:
			continue
		if stages and s.get("stage") not in selected_stages:
			continue
		if min_score > 0 and (score_num is None or score_num < min_score):
			continue

		if score_num is not None:
			scores_numeric.append(score_num)
		filtered.append((s, analysis, score_num))

	col_m1, col_m2, col_m3 = st.columns(3)
	with col_m1:
		st.metric("Total startups", len(filtered))
	with col_m2:
		avg_score = round(sum(scores_numeric) / len(scores_numeric), 1) if scores_numeric else "-"
		st.metric("Average score", avg_score)
	with col_m3:
		ready_count = sum(1 for _, a, _ in filtered if "ready" in str(a.get("investor_readiness", "")).lower())
		st.metric("Investor-ready", ready_count)

	st.markdown("---")
	if shortlist_enabled and "shortlist" not in st.session_state:
		st.session_state["shortlist"] = set()

	for s, analysis, score_num in filtered:
		header = f"{s.get('name', '')} • {s.get('industry', '')} • {s.get('stage', '')}"
		score_label = analysis.get("score", "N/A")
		with st.expander(f"{header}  (Score: {score_label})"):
			col_a, col_b = st.columns([2, 1])
			with col_a:
				st.write("**Problem:**", s.get("problem", ""))
				st.write("**Solution:**", s.get("solution", ""))
				st.write("**Target market:**", s.get("target_market", ""))
			with col_b:
				st.write("**Founder:**", s.get("founder", ""))
				st.write("**Investor readiness:**", analysis.get("investor_readiness", ""))
				st.write("**Investor recommendation:**", analysis.get("investor_recommendation", ""))

			if shortlist_enabled:
				btn_label = "Shortlist" if s["id"] not in st.session_state["shortlist"] else "Remove from shortlist"
				if st.button(btn_label, key=f"shortlist_{s['id']}"):
					if s["id"] in st.session_state["shortlist"]:
						st.session_state["shortlist"].remove(s["id"])
					else:
						st.session_state["shortlist"].add(s["id"])

			summary = analysis.get("summary", "")
			if summary:
				st.markdown("**AI summary**")
				st.caption(summary)

			strengths = analysis.get("strengths", []) or []
			weaknesses = analysis.get("weaknesses", []) or []
			risks = analysis.get("risks", []) or []

			cols_lists = st.columns(3)
			with cols_lists[0]:
				if strengths:
					st.markdown("**Strengths**")
					for item in strengths:
						st.write(f"- {item}")
			with cols_lists[1]:
				if weaknesses:
					st.markdown("**Weaknesses**")
					for item in weaknesses:
						st.write(f"- {item}")
			with cols_lists[2]:
				if risks:
					st.markdown("**Risks**")
					for item in risks:
						st.write(f"- {item}")

	if shortlist_enabled and st.session_state.get("shortlist"):
		st.markdown("---")
		st.markdown("#### Shortlist")
		shortlisted = [s for s in startups if s.get("id") in st.session_state["shortlist"]]
		if shortlisted:
			rows = [
				{
					"Name": s.get("name", ""),
					"Industry": s.get("industry", ""),
					"Stage": s.get("stage", ""),
					"Score": (s.get("analysis", {}) or {}).get("score", "N/A"),
				}
				for s in shortlisted
			]
			st.dataframe(rows, use_container_width=True)


def render_manage_startups() -> None:
	"""Admin/accelerator-style CRUD view for startups."""
	global startups
	if not startups:
		st.info("No startups to manage yet. Use the Founder workspace to create one.")
		return

	options = {}
	for s in startups:
		label = f"{s.get('name', '')} • {s.get('industry', '')} • {s.get('stage', '')} (ID {s.get('id')})"
		options[label] = s.get("id")

	selected_label = st.selectbox("Select a startup", list(options.keys()))
	selected_id = options[selected_label]
	selected_startup = next((s for s in startups if int(s.get("id", -1)) == int(selected_id)), None)
	if selected_startup is None:
		st.error("Could not find the selected startup.")
		return

	with st.form("edit_startup_form"):
		st.markdown("##### Edit startup profile")
		col1, col2 = st.columns(2)
		with col1:
			name = st.text_input("Startup Name", value=selected_startup.get("name", ""))
			founder = st.text_input("Founder Name", value=selected_startup.get("founder", ""))
			industry = st.text_input("Industry", value=selected_startup.get("industry", ""))
			stage = st.selectbox(
				"Stage",
				["Idea", "MVP", "Pre-seed", "Seed", "Series A+"],
				index=["Idea", "MVP", "Pre-seed", "Seed", "Series A+"].index(selected_startup.get("stage", "MVP")),
			)
		with col2:
			problem = st.text_area("Problem", value=selected_startup.get("problem", ""), height=80)
			solution = st.text_area("Solution", value=selected_startup.get("solution", ""), height=80)
			target_market = st.text_area("Target Market", value=selected_startup.get("target_market", ""), height=80)

		deal_stage_options = [
			"Submitted",
			"Screening",
			"Meeting",
			"Diligence",
			"Offer",
			"Invested",
			"Declined",
		]
		current_deal_stage = selected_startup.get("deal_stage", "Submitted")
		if current_deal_stage not in deal_stage_options:
			current_deal_stage = "Submitted"
		deal_stage = st.selectbox("Deal stage", deal_stage_options, index=deal_stage_options.index(current_deal_stage))
		try:
			current_invested = float(selected_startup.get("invested_amount", 0) or 0)
		except Exception:
			current_invested = 0.0
		invested_amount = st.number_input("Invested amount (USD)", min_value=0.0, value=current_invested, step=1000.0)

		pitch_text = st.text_area("Pitch text (used for analysis)", value=selected_startup.get("pitch_text", ""), height=150)
		update_clicked = st.form_submit_button("Save Changes")

	if update_clicked:
		updated_fields = {
			"name": name.strip(),
			"founder": founder.strip(),
			"industry": industry.strip(),
			"stage": stage,
			"problem": problem.strip(),
			"solution": solution.strip(),
			"target_market": target_market.strip(),
			"deal_stage": deal_stage,
			"invested_amount": invested_amount,
			"pitch_text": pitch_text.strip(),
		}
		startups = backend_api.update_startup(selected_id, updated_fields)
		st.success("Startup updated in JSON database.")

	col_del, _ = st.columns([1, 3])
	with col_del:
		if st.button("Delete startup", type="primary"):
			startups = backend_api.delete_startup(selected_id)
			st.success("Startup deleted.")
			st.stop()


def render_networking_board(editable: bool = True) -> None:
	"""Founder networking board; when editable, show post form."""
	global networking_posts
	if editable:
		with st.form("networking_form"):
			founder_name = st.text_input("Founder name")
			startup_name = st.text_input("Startup name")
			looking_for = st.selectbox(
				"Looking for",
				["Investor", "Cofounder", "Developer", "Mentor", "Early adopters", "Other"],
			)
			message = st.text_area(
				"Short message",
				placeholder="What kind of help or connection are you looking for?",
				height=120,
			)
			submit_post = st.form_submit_button("Post to networking board")

		if submit_post:
			if not founder_name or not message:
				st.warning("Please provide at least your name and a message.")
			else:
				post = {
					"founder_name": founder_name.strip(),
					"startup_name": startup_name.strip(),
					"looking_for": looking_for,
					"message": message.strip(),
				}
				networking_posts = backend_api.create_networking_post(post)
				st.success("Posted to networking board.")

	st.markdown("###### Networking board")
	if not networking_posts:
		st.info("No networking posts yet. Be the first to post!")
	else:
		for post in reversed(networking_posts):
			with st.container(border=True):
				col_h, col_tag = st.columns([3, 1])
				with col_h:
					st.markdown(f"**{post.get('founder_name', '')}** · {post.get('startup_name', '')}")
				with col_tag:
					st.caption(f"Looking for: {post.get('looking_for', '')}")
				st.write(post.get("message", ""))
				st.caption(post.get("created_at", ""))


def render_ai_assistant_panel(active_role: str) -> None:
	"""AI assistant panel: quick pitch evaluation + role-aware Q&A with demo mode fallback."""
	role_prompt = {
		"Founder": "You are a concise startup mentor helping founders refine pitches, clarify problem/solution, and become investor-ready.",
		"Investor": "You are an analytical early-stage investor helping evaluate and compare startups for potential investment.",
		"Developer": "You are a technical mentor helping developers evaluate startup teams and opportunities to join.",
		"Accelerator": "You advise accelerators on portfolio quality, selection, and ecosystem orchestration.",
	}.get(active_role, "You are a concise startup mentor for founders and investors.")

	st.markdown("##### AI Startup Assistant")
	left, right = st.columns([2, 1])
	with left:
		st.markdown("Submit a short pitch and get structured AI feedback.")
		pitch = st.text_area("Quick pitch text", height=140)
		if st.button("Analyze pitch", key=f"ai_assistant_analyze_{active_role}"):
			if not pitch.strip():
				st.warning("Please paste a pitch.")
			else:
				startup = {
					"name": "Ad-hoc pitch",
					"founder": "",
					"industry": "",
					"stage": "MVP",
					"problem": "",
					"solution": "",
					"target_market": "",
					"pitch_text": pitch.strip(),
				}
				with st.spinner("Running AI evaluation..."):
					analysis = backend_api.ai_evaluate_startup(startup)
				st.json(analysis)

	with right:
		st.markdown("Assistant insight")
		placeholder = {
			"Founder": "Ask the assistant (e.g. 'How do I improve my seed pitch?')",
			"Investor": "Ask the assistant (e.g. 'What signals matter for this startup?')",
			"Developer": "Ask the assistant (e.g. 'Is this a good team for me?')",
			"Accelerator": "Ask the assistant (e.g. 'Which startups are Demo Day ready?')",
		}.get(active_role, "Ask the assistant a startup question")
		context_question = st.text_area(placeholder, height=140)
		if st.button("Ask AI", key=f"ai_assistant_chat_{active_role}"):
			if not context_question.strip():
				st.warning("Please enter a question.")
			else:
				try:
					response = backend_api.ai_assistant({"role": role, "question": context_question})
					st.write(response.get("answer", "No response from AI assistant."))
				except Exception:
					st.info("AI is in demo mode. This is a mock answer.")
					st.write("This startup is promising but needs more traction. Focus on clarifying the business model and highlighting team strengths.")


# --- Main sections ---
render_hero(role)

if section == "Dashboard":
	# Accelerator gets the richest dashboard; others get a lighter summary.
	render_kpi_row()
	if role == "Accelerator":
		col_left, col_right = st.columns([2, 1])
		with col_left:
			st.markdown(" ")
			st.markdown("<div class='widget-title'>Startup pipeline</div>", unsafe_allow_html=True)
			st.markdown("<div class='widget-caption'>Latest evaluated companies in your portfolio.</div>", unsafe_allow_html=True)
			if startups:
				import pandas as pd
				# Chart: Startups by deal stage
				stage_counts = {}
				for s in startups:
					stage = s.get("deal_stage", s.get("stage", "Submitted"))
					stage_counts[stage] = stage_counts.get(stage, 0) + 1
				chart_df = pd.DataFrame({"Stage": list(stage_counts.keys()), "Count": list(stage_counts.values())})
				st.bar_chart(chart_df.set_index("Stage"), use_container_width=True, color="#38bdf8")
				for s in list(reversed(startups))[:2]:
					render_startup_profile_card(s)
			else:
				st.markdown('<div class="card-subtle" style="text-align:center; padding:2.2rem 1rem;">'
							'<div style="font-size:2.2rem;">✨</div>'
							'<div style="font-size:1.1rem; font-weight:600; margin-top:8px;">No startups yet</div>'
							'<div style="color:#bae6fd; margin-top:4px;">Add your first startup from the Startups section.</div>'
							'</div>', unsafe_allow_html=True)
		with col_right:
			st.markdown(" ")
			with st.container(border=True):
				st.markdown("<div class='widget-title'>AI insights <span style='float:right;'>🤖</span></div>", unsafe_allow_html=True)
				st.caption("Quick snapshot of your latest AI evaluations.")
				if startups:
					latest = list(reversed(startups))[0]
					analysis = (latest.get("analysis") or {})
					st.markdown(f"<div style='font-size:1.1rem; font-weight:600;'>{latest.get('name','')}</div>", unsafe_allow_html=True)
					st.markdown(f"<div style='color:#38bdf8; font-size:1.2rem; font-weight:700;'>Score: {analysis.get('score','N/A')}</div>", unsafe_allow_html=True)
					st.markdown(f"<div style='color:#bae6fd; font-size:0.98rem;'>Investor readiness: {analysis.get('investor_readiness','')}</div>", unsafe_allow_html=True)
				else:
					st.caption("No AI evaluations yet.")
			with st.container(border=True):
				st.markdown("<div class='widget-title' style='margin-top:6px;'>Upcoming events <span style='float:right;'>📅</span></div>", unsafe_allow_html=True)
				from_events = events or []
				if from_events:
					for ev in from_events[:3]:
						st.markdown(f"<div style='margin-bottom:6px;'><span class='icon-badge' style='font-size:1.1rem;'>📍</span> <b>{ev.get('name','')}</b> <span style='color:#bae6fd;'>· {ev.get('date','')}</span></div>", unsafe_allow_html=True)
				else:
					st.caption("No events scheduled – create one from the Events tab.")
			with st.container(border=True):
				st.markdown("<div class='widget-title' style='margin-top:6px;'>Today&apos;s focus <span style='float:right;'>📝</span></div>", unsafe_allow_html=True)
				st.caption("Suggested actions for your team.")
				st.markdown("<ul style='margin-left:-1.2em; color:#bae6fd; font-size:1.01rem;'><li>Review startups with highest AI scores.</li><li>Move ready companies to Demo Day or Offer.</li><li>Invite key investors to the next event.</li></ul>", unsafe_allow_html=True)
	else:
		col_left, col_right = st.columns([2, 1])
		with col_left:
			st.markdown(" ")
			# Outlined card for Getting started
			st.markdown(
				"""
				<div style='background: rgba(16,23,42,0.85); border: 2px solid #38bdf8; border-radius: 18px; padding: 1.5rem 1.2rem; margin-bottom: 18px; box-shadow: 0 2px 16px #0ea5e922;'>
					<div style='font-size:1.1rem; font-weight:700; color:#fff; margin-bottom:8px;'>Getting started</div>
					<ul style='color:#bae6fd; font-size:1.01rem; margin:0 0 0 1.2em;'>
				"""
				+ ("<li>Create your startup profile from the My Startup or AI Assistant sections.</li>\n<li>Run an AI evaluation to understand investor readiness.</li>\n<li>Post to Networking to meet investors and builders.</li>" if role == "Founder" else
				   "<li>Browse the Startup Directory and shortlist promising teams.</li>\n<li>Use Deal Flow to understand where deals sit in the pipeline.</li>" if role == "Investor" else
				   "<li>Create your developer profile so founders can discover you.</li>\n<li>Check Opportunities for teams looking for technical help.</li>" if role == "Developer" else
				   "<li>Monitor portfolio health and upcoming ecosystem events.</li>")
				+ """
					</ul>
				</div>
				""",
				unsafe_allow_html=True,
			)
		with col_right:
			st.markdown(" ")
			# Outlined card for Next steps
			st.markdown(
				"""
				<div style='background: rgba(16,23,42,0.85); border: 2px solid #38bdf8; border-radius: 18px; padding: 1.5rem 1.2rem; margin-bottom: 18px; box-shadow: 0 2px 16px #0ea5e922;'>
					<div style='font-size:1.1rem; font-weight:700; color:#fff; margin-bottom:8px;'>Next steps</div>
					<ul style='color:#bae6fd; font-size:1.01rem; margin:0 0 0 1.2em;'>
				"""
				+ ("<li>Prepare an updated pitch for your next investor call.</li>\n<li>Use the AI Assistant to refine your deck narrative.</li>" if role == "Founder" else
				   "<li>Shortlist 3–5 startups to track more closely.</li>\n<li>Ask the AI Assistant for red flags and strengths.</li>" if role == "Investor" else
				   "<li>Reach out to 1–2 founders that fit your interests.</li>\n<li>Use the AI Assistant to assess a startup before joining.</li>" if role == "Developer" else
				   "<li>Align team on which startups to push toward Demo Day.</li>\n<li>Invite key mentors and investors to upcoming events.</li>")
				+ """
					</ul>
				</div>
				""",
				unsafe_allow_html=True,
			)


elif role == "Founder" and section == "My Startup":
	# All logic below can now safely assign to startups
	st.markdown("### My Startup Profile")
	founder_startup = startups[-1] if startups else None
	def render_startup_full_form(existing=None):
		st.markdown("#### Create or Edit Your Startup Profile")
		with st.form("founder_startup_form"):
			col1, col2 = st.columns(2)
			with col1:
				name = st.text_input("Startup Name", value=existing.get("name", "") if existing else "")
				founder = st.text_input("Founder Name", value=existing.get("founder", "") if existing else "")
				industry = st.text_input("Industry / Sector", value=existing.get("industry", "") if existing else "")
				stage = st.selectbox(
					"Stage",
					["Idea", "MVP", "Pre-seed", "Seed", "Series A+"],
					index=["Idea", "MVP", "Pre-seed", "Seed", "Series A+"].index(existing.get("stage", "MVP")) if existing else 1,
				)
				business_model = st.text_input("Business Model", value=existing.get("business_model", "") if existing else "")
				traction = st.text_input("Traction", value=existing.get("traction", "") if existing else "")
			with col2:
				problem = st.text_area("Problem", value=existing.get("problem", "") if existing else "", height=80)
				solution = st.text_area("Solution", value=existing.get("solution", "") if existing else "", height=80)
				target_market = st.text_area("Target Market", value=existing.get("target_market", "") if existing else "", height=80)
				funding_ask = st.text_input("Funding Ask (USD)", value=existing.get("funding_ask", "") if existing else "")
			st.markdown("---")
			st.markdown("**Pitch**")
			pitch_text = st.text_area("Pitch Text", value=existing.get("pitch_text", "") if existing else "", height=120)
			pitch_pdf = st.file_uploader("Optional: Upload Pitch Deck (PDF)", type=["pdf"])
			submit_label = "Update Startup & Re-run AI" if existing else "Create Startup & Run AI"
			submitted = st.form_submit_button(submit_label)
		return {
			"submitted": submitted,
			"name": name,
			"founder": founder,
			"industry": industry,
			"stage": stage,
			"problem": problem,
			"solution": solution,
			"target_market": target_market,
			"business_model": business_model,
			"traction": traction,
			"funding_ask": funding_ask,
			"pitch_text": pitch_text,
			"pitch_pdf": pitch_pdf,
		}

	def extract_text_from_pdf(pdf_file):
		try:
			reader = PyPDF2.PdfReader(pdf_file)
			text = "\n".join(page.extract_text() or "" for page in reader.pages)
			return text.strip()
		except Exception:
			return ""

	if not founder_startup:
		st.markdown('<div class="card" style="margin-bottom:18px;text-align:center;"><div style="font-size:1.5rem;">🚀</div><div style="font-size:1.1rem;font-weight:600;margin-top:8px;">Create your startup profile to begin</div><div style="color:#bae6fd;margin-top:4px;">Fill out the form below to get AI feedback and unlock all features.</div></div>', unsafe_allow_html=True)
		form = render_startup_full_form()
		if form["submitted"]:
			# Handle PDF pitch deck
			pitch_text_val = form["pitch_text"]
			if form["pitch_pdf"]:
				pdf_text = extract_text_from_pdf(form["pitch_pdf"])
				if pdf_text:
					pitch_text_val = pdf_text
			if not form["name"] or not form["industry"] or not form["stage"]:
				st.warning("Please fill at least Startup Name, Industry, and Stage.")
			elif not pitch_text_val.strip():
				st.warning("Please provide pitch text or upload a PDF.")
			else:
				startup = {
					"name": form["name"].strip(),
					"founder": form["founder"].strip(),
					"industry": form["industry"].strip(),
					"stage": form["stage"],
					"problem": form["problem"].strip(),
					"solution": form["solution"].strip(),
					"target_market": form["target_market"].strip(),
					"business_model": form["business_model"].strip(),
					"traction": form["traction"].strip(),
					"funding_ask": form["funding_ask"].strip(),
					"pitch_text": pitch_text_val.strip(),
				}
				with st.spinner("Analyzing startup with AI..."):
					analysis = backend_api.ai_evaluate_startup(startup)
				startup["analysis"] = analysis
				startups = backend_api.create_startup(startup)
				st.success("Startup created and analyzed!")
				founder_startup = startup
	else:
		st.markdown("<div class='card' style='margin-bottom:18px;'><b>Your Startup Profile</b></div>", unsafe_allow_html=True)
		render_startup_profile_card(founder_startup)
		analysis = founder_startup.get("analysis", {}) or {}
		with st.expander("Show full AI evaluation", expanded=True):
			col_left, col_right = st.columns([2, 1])
			with col_left:
				st.markdown("###### Startup profile")
				render_startup_profile_card(founder_startup)
			with col_right:
				st.markdown("###### AI score")
				score_value = analysis.get("score", "N/A")
				st.metric("Overall Score /10", str(score_value))
				st.write("**Investor readiness:**")
				st.write(analysis.get("investor_readiness", ""))
			st.markdown("---")
			st.markdown("###### AI evaluation breakdown")
			col_b1, col_b2 = st.columns(2)
			with col_b1:
				st.write("**Problem clarity:**", analysis.get("problem_clarity", ""))
				st.write("**Solution strength:**", analysis.get("solution_strength", ""))
				st.write("**Market potential:**", analysis.get("market_potential", ""))
			with col_b2:
				st.write("**Business model clarity:**", analysis.get("business_model", ""))
				st.write("**Investor recommendation:**", analysis.get("investor_recommendation", ""))
			summary = analysis.get("summary", "")
			if summary:
				st.markdown("**Summary**")
				st.info(summary)
			strengths = analysis.get("strengths", []) or []
			weaknesses = analysis.get("weaknesses", []) or []
			risks = analysis.get("risks", []) or []
			suggestions = analysis.get("suggestions", []) or []
			cols_lists = st.columns(3)
			with cols_lists[0]:
				if strengths:
					st.markdown("**Strengths**")
					for item in strengths:
						st.write(f"- {item}")
			with cols_lists[1]:
				if weaknesses:
					st.markdown("**Weaknesses**")
					for item in weaknesses:
						st.write(f"- {item}")
			with cols_lists[2]:
				if risks:
					st.markdown("**Risks**")
					for item in risks:
						st.write(f"- {item}")
			if suggestions:
				st.markdown("**Suggestions for improvement**")
				for item in suggestions:
					st.write(f"- {item}")
		st.markdown("---")
		st.markdown("#### Edit or Update Your Startup Profile")
		form = render_startup_full_form(existing=founder_startup)
		if form["submitted"]:
			pitch_text_val = form["pitch_text"]
			if form["pitch_pdf"]:
				pdf_text = extract_text_from_pdf(form["pitch_pdf"])
				if pdf_text:
					pitch_text_val = pdf_text
			if not form["name"] or not form["industry"] or not form["stage"]:
				st.warning("Please fill at least Startup Name, Industry, and Stage.")
			elif not pitch_text_val.strip():
				st.warning("Please provide pitch text or upload a PDF.")
			else:
				updated = {
					"name": form["name"].strip(),
					"founder": form["founder"].strip(),
					"industry": form["industry"].strip(),
					"stage": form["stage"],
					"problem": form["problem"].strip(),
					"solution": form["solution"].strip(),
					"target_market": form["target_market"].strip(),
					"business_model": form["business_model"].strip(),
					"traction": form["traction"].strip(),
					"funding_ask": form["funding_ask"].strip(),
					"pitch_text": pitch_text_val.strip(),
				}
				with st.spinner("Re-running AI evaluation..."):
					analysis = backend_api.ai_evaluate_startup(updated)
				updated["analysis"] = analysis
				startups = backend_api.update_startup(founder_startup["id"], updated)
				st.success("Startup updated and re-analyzed!")

elif role == "Founder" and section == "AI Assistant":
	st.markdown("### AI Assistant for founders")
	render_ai_assistant_panel(role)

elif role == "Founder" and section == "Networking":
	st.markdown("### Founder networking")
	render_networking_board(editable=True)

elif role == "Founder" and section == "Events":
	st.markdown("### Events for founders")
	from_events = globals().get("events", []) if "events" in globals() else []
	if from_events:
		for ev in from_events:
			st.write(f"- {ev.get('name','')} · {ev.get('date','')}")
	else:
		st.caption("No events yet – accelerators can create them from the Accelerator role.")

elif role == "Investor" and section == "Startup Directory":
	st.markdown("### Startup Directory")
	st.caption("Browse analyzed startups, filter by signals, and inspect AI evaluations.")
	render_directory_table(shortlist_enabled=True)

elif role == "Investor" and section == "Shortlist":
	st.markdown("### My shortlist")
	if st.session_state.get("shortlist"):
		shortlisted = [s for s in startups if s.get("id") in st.session_state["shortlist"]]
		if shortlisted:
			rows = [
				{
					"Name": s.get("name", ""),
					"Industry": s.get("industry", ""),
					"Stage": s.get("stage", ""),
					"Score": (s.get("analysis", {}) or {}).get("score", "N/A"),
				}
				for s in shortlisted
			]
			st.dataframe(rows, use_container_width=True)
		else:
			st.info("No startups in shortlist yet – add some from the Startup Directory.")
	else:
		st.info("Your shortlist is empty – add startups from the Startup Directory.")

elif role == "Investor" and section == "Deal Flow":
	st.markdown("### Deal flow overview")
	st.caption("Pipeline by deal stage with capital deployed.")
	if not startups:
		st.info("No startups in pipeline yet.")
	else:
		stages = {}
		total_invested = 0.0
		for s in startups:
			stage = s.get("deal_stage", s.get("stage", "Submitted"))
			stages.setdefault(stage, 0)
			stages[stage] += 1
			try:
				amt = float(s.get("invested_amount", 0) or 0)
			except Exception:
				amt = 0.0
			total_invested += amt
		col_l, col_r = st.columns([2, 1])
		with col_l:
			st.markdown("<div class='widget-title'>Pipeline by stage</div>", unsafe_allow_html=True)
			rows = [{"Deal stage": k, "Count": v} for k, v in stages.items()]
			st.dataframe(rows, use_container_width=True)
		with col_r:
			st.markdown("<div class='widget-title'>Capital deployed</div>", unsafe_allow_html=True)
			st.metric("Total invested (approx)", f"${total_invested:,.0f}")

elif role == "Investor" and section == "Events":
	st.markdown("### Investor events")
	from_events = globals().get("events", []) if "events" in globals() else []
	if from_events:
		for ev in from_events:
			st.write(f"- {ev.get('name','')} · {ev.get('date','')}")
	else:
		st.caption("No events yet – accelerators can create them from the Accelerator role.")

elif role == "Developer" and section == "My Profile":
	st.markdown("### My Developer Profile")
	from_devs = developers if "developers" in globals() else []
	current = from_devs[-1] if from_devs else None
	with st.form("dev_profile_form"):
		name = st.text_input("Name", value=current.get("name", "") if current else "")
		skills = st.text_input("Skills (comma-separated)", value=current.get("skills", "") if current else "")
		preferred_roles = st.text_input("Preferred roles", value=current.get("preferred_roles", "") if current else "")
		preferred_stage = st.text_input("Preferred startup stage", value=current.get("preferred_startup_stage", "") if current else "")
		availability = st.text_input("Availability", value=current.get("availability", "") if current else "")
		portfolio_link = st.text_input("Portfolio link", value=current.get("portfolio_link", "") if current else "")
		bio = st.text_area("Short bio", value=current.get("bio", "") if current else "", height=100)
		sub = st.form_submit_button("Save profile")

	st.caption("See who is looking for technical help or cofounders.")
	if not networking_posts:
		st.info("No networking posts yet.")
	else:
		for post in reversed(networking_posts):
			if "developer" not in str(post.get("looking_for", "")).lower():
				continue
			with st.container(border=True):
				col_h, col_tag = st.columns([3, 1])
				with col_h:
					st.markdown(f"**{post.get('founder_name', '')}** · {post.get('startup_name', '')}")
				with col_tag:
					st.caption(f"Looking for: {post.get('looking_for', '')}")
				st.write(post.get("message", ""))
				st.caption(post.get("created_at", ""))

elif role == "Developer" and section == "Networking":
	st.markdown("### Networking for developers")
	render_networking_board(editable=False)

elif role == "Developer" and section == "AI Assistant":
	st.markdown("### AI Assistant for developers")
	render_ai_assistant_panel(role)

elif role == "Developer" and section == "Events":
	st.markdown("### Developer events")
	from_events = globals().get("events", []) if "events" in globals() else []
	if from_events:
		for ev in from_events:
			st.write(f"- {ev.get('name','')} · {ev.get('date','')}")
	else:
		st.caption("No events yet – accelerators can create them from the Accelerator role.")

elif role == "Accelerator" and section == "Startups":
	st.markdown("### Startups (portfolio & pipeline)")
	startup_tabs = st.tabs([
		"Profiles",
		"Manage (CRUD)",
	])
	with startup_tabs[0]:
		if startups:
			for s in startups:
				render_startup_profile_card(s)
		else:
			st.info("No startups yet – onboard founders from the Founder role.")
	with startup_tabs[1]:
		st.markdown("##### Manage startup profiles (CRUD)")
		render_manage_startups()

elif role == "Accelerator" and section == "Investors":
	st.markdown("### Investors")
	from_investors = investors if "investors" in globals() else []
	with st.form("investor_form"):
		name = st.text_input("Name")
		firm = st.text_input("Firm")
		sector_interests = st.text_input("Sector interests")
		stage_pref = st.text_input("Stage preference")
		ticket_size = st.text_input("Ticket size (range)")
		location = st.text_input("Location")
		bio = st.text_area("Short bio", height=100)
		sub = st.form_submit_button("Add investor")

	if sub:
		inv = {
			"name": name.strip(),
			"firm": firm.strip(),
			"sector_interests": sector_interests.strip(),
			"stage_preference": stage_pref.strip(),
			"ticket_size": ticket_size.strip(),
			"location": location.strip(),
			"bio": bio.strip(),
		}
		investors = backend_api.create_investor(inv)
		st.success("Investor added.")

	if investors:
		rows = [
			{
				"Name": i.get("name", ""),
				"Firm": i.get("firm", ""),
				"Sectors": i.get("sector_interests", ""),
				"Stages": i.get("stage_preference", ""),
				"Ticket size": i.get("ticket_size", ""),
			}
			for i in investors
		]
		st.dataframe(rows, use_container_width=True)

elif role == "Accelerator" and section == "Developers":
	st.markdown("### Developers")
	from_devs = developers if "developers" in globals() else []
	if from_devs:
		rows = [
			{
				"Name": d.get("name", ""),
				"Skills": d.get("skills", ""),
				"Preferred roles": d.get("preferred_roles", ""),
				"Stage": d.get("preferred_startup_stage", ""),
			}
			for d in from_devs
		]
		st.dataframe(rows, use_container_width=True)
	else:
		st.caption("No developer profiles yet – developers can create them from the Developer role.")

elif role == "Accelerator" and section == "Deal Flow":
	st.markdown("### Deal flow overview")
	st.caption("Portfolio pipeline by deal stage with total invested amount.")
	if not startups:
		st.info("No startups in pipeline yet.")
	else:
		stages = {}
		total_invested = 0.0
		for s in startups:
			stage = s.get("deal_stage", s.get("stage", "Submitted"))
			stages.setdefault(stage, 0)
			stages[stage] += 1
			try:
				amt = float(s.get("invested_amount", 0) or 0)
			except Exception:
				amt = 0.0
			total_invested += amt
		col_l, col_r = st.columns([2, 1])
		with col_l:
			st.markdown("<div class='widget-title'>Pipeline by stage</div>", unsafe_allow_html=True)
			rows = [{"Deal stage": k, "Count": v} for k, v in stages.items()]
			st.dataframe(rows, use_container_width=True)
		with col_r:
			st.markdown("<div class='widget-title'>Capital deployed</div>", unsafe_allow_html=True)
			st.metric("Total invested", f"${total_invested:,.0f}")

elif role == "Accelerator" and section == "Events":
	st.markdown("### Ecosystem events (manage)")
	from_events = events if "events" in globals() else []
	with st.form("event_form"):
		name = st.text_input("Event name")
		date = st.text_input("Date")
		etype = st.text_input("Type (Demo Day, Office Hours, etc.)")
		location = st.text_input("Location")
		desc = st.text_area("Description", height=80)
		sub = st.form_submit_button("Add event")

	if sub:
		new_event = {
			"name": name.strip(),
			"date": date.strip(),
			"type": etype.strip(),
			"location": location.strip(),
			"description": desc.strip(),
		}
		events = backend_api.create_event(new_event)
		st.success("Event created.")

	st.markdown("#### Upcoming events")
	if events:
		for ev in events:
			with st.container(border=True):
				st.markdown(f"**{ev.get('name','')}** · {ev.get('date','')} · {ev.get('location','')}")
				st.caption(ev.get("type", ""))
				st.write(ev.get("description", ""))
	else:
		st.caption("No events yet.")

elif role == "Accelerator" and section == "AI Assistant":
	st.markdown("### AI Assistant for accelerators")
	render_ai_assistant_panel(role)

elif role == "Investor" and section == "AI Assistant":
	st.markdown("### AI Assistant for investors")
	render_ai_assistant_panel(role)

