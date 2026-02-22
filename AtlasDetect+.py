import customtkinter as ctk
import plotly.graph_objects as go
import time, random, os, webbrowser, threading

ctk.set_appearance_mode("dark")

class AtlasApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("ATLAS DETECT v8.1 [DECOY FILTER]")
        self.geometry("600x850")
        self.resizable(False, False)

        self.label = ctk.CTkLabel(self, text="ATLAS INTELLIGENCE TERMINAL", font=("Courier New", 24, "bold"), text_color="#00FF00")
        self.label.pack(pady=20)

        self.entry = ctk.CTkEntry(self, placeholder_text="ENTER TARGET ID...", width=450, height=50, font=("Courier New", 18), border_color="#00FF00", text_color="#00FF00")
        self.entry.pack(pady=10)

        self.btn = ctk.CTkButton(self, text="INITIATE TRACE", command=self.start_scan, 
                                fg_color="transparent", border_width=2, text_color="#00FF00", 
                                hover_color="#1a331a", font=("Courier New", 18, "bold"))
        self.btn.pack(pady=20)

        self.progress = ctk.CTkProgressBar(self, width=500, progress_color="#00FF00")
        self.progress.set(0)
        self.progress.pack(pady=10)

        self.console = ctk.CTkTextbox(self, width=540, height=400, font=("Courier New", 12), text_color="#00FF00", border_color="#004400", border_width=1)
        self.console.pack(pady=20)
        
        self.spinner_label = ctk.CTkLabel(self, text="[ / ]", font=("Courier New", 14), text_color="#00FF00")
        self.spinner_label.place(relx=0.9, rely=0.97)
        
        self.stop_spinner = False
        threading.Thread(target=self.animate_spinner, daemon=True).start()

    def animate_spinner(self):
        chars = ["[/]", "[-]", "[\\]", "[|]"]
        i = 0
        while not self.stop_spinner:
            self.spinner_label.configure(text=chars[i])
            i = (i + 1) % 4
            time.sleep(0.2)

    def log(self, text):
        self.console.configure(state="normal")
        self.console.insert("end", f"> {text}\n")
        self.console.see("end")
        self.console.configure(state="disabled")
        self.update()

    def start_scan(self):
        target = self.entry.get().strip()
        if not target: return
        self.btn.configure(state="disabled")
        self.console.configure(state="normal", border_color="#00FF00")
        self.console.delete("1.0", "end")
        self.console.configure(state="disabled")

        logs = [
            f"IDENTIFYING TARGET: {target.upper()}",
            f"IDENTIFYING TARGET: {target.upper()}",
            "SEARCHING FOR NEURAL LINKS...",
            "connection: agent happy goose...",
            "detect fake IP addresses...",
            "FILTERING DECOY SIGNALS...",
            "BYPASSING KERNEL RING-0...",
            "NODE_01: CONNECTION OK",
            "DECRYPTING RSA-8192 PACKETS...",
            "connections to the !atlas! server...",
            "INJECTING SHELLCODE v4.2...",
            "object focus...",
            "loading atlas pockets...",
            "SATELLITE SYNC: 99.8%",
            "ANALYZING TRAFFIC PATTERNS...",
            "object detected!!!...",
            "Trace complete. Agent 'Happy Goose' linked to the stream"
        ]

        for i, m in enumerate(logs):
            self.log(m)
            steps = 15
            for s in range(1, steps + 1):
                self.progress.set((i * steps + s) / (len(logs) * steps))
                self.update()
                time.sleep(0.01)
        
        self.progress.set(1.0)
        self.generate_report(target)
        self.btn.configure(state="normal")
        self.console.configure(border_color="#004400")

    def generate_report(self, target):
        fig = go.Figure()
        sync = random.randint(0, 100)
        
        # 1. ТУСКЛЫЕ ФАЛЬШИВЫЕ ЦЕЛИ (Не соединены линиями)
        dx = [random.uniform(-1.5, 1.5) for _ in range(6)]
        dy = [random.uniform(-1.5, 1.5) for _ in range(6)]
        fig.add_trace(go.Scatter(x=dx, y=dy, mode='markers', 
                                 marker=dict(size=9, symbol='diamond', color='#004400'),
                                 text=["[SIGNAL DECOY]"]*6, hoverinfo="text"))

        # 2. ОСНОВНОЙ МАРШРУТ (С линиями)
        px = [random.uniform(-1.3, 1.3) for _ in range(7)]
        py = [random.uniform(-1.3, 1.3) for _ in range(7)]
        points = sorted(zip(px, py), key=lambda p: (p[0]**2 + p[1]**2))
        px_s, py_s = zip(*points)
        
        fig.add_trace(go.Scatter(x=px_s, y=py_s, mode='lines+markers', 
                                 line=dict(color='#00FF00', width=1.5, dash='dot'), 
                                 marker=dict(size=12, symbol='diamond-open', color='#00FF00'),
                                 text=[f"NODE ACTIVE: {random.randint(10,99)}%" for _ in range(7)], hoverinfo="text"))
        
        # Центр
        fig.add_trace(go.Scatter(x=[0], y=[0], mode='markers', 
                                 marker=dict(size=22, symbol='star', color='#00FF00', line=dict(width=2, color="white"))))

        # Сетка
        for r in [0.3, 0.6, 0.9, 1.2, 1.5]:
            fig.add_shape(type="circle", x0=-r, y0=-r, x1=r, y1=r, line=dict(color="#00FF00", width=1), opacity=0.1)

        # Инфо-блок
        fig.add_annotation(
            text=f"<b>ATLAS REPORT: {target.upper()}</b><br>STATUS: COMPROMISED<br>DECOYS FILTERED: 6<br>-----------------------<br>SYNC: {sync}%<br>OP ID: happy_goose",
            font=dict(family="Courier New", size=18, color="#00FF00"),
            showarrow=False, bgcolor="black", bordercolor="#00FF00", borderwidth=1, borderpad=15,
            xref="paper", yref="paper", x=0.02, y=0.98, align="left"
        )

        fig.update_layout(template="plotly_dark", paper_bgcolor="black", plot_bgcolor="black", 
                          yaxis=dict(visible=False, scaleanchor="x", scaleratio=1), xaxis=dict(visible=False), margin=dict(l=0, r=0, t=0, b=0), showlegend=False)

        filename = "atlas_decoy_report.html"
        fig.write_html(filename)
        webbrowser.open(f"file://{os.path.abspath(filename)}")

if __name__ == "__main__":
    app = AtlasApp()
    app.mainloop()


