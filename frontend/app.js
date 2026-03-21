let adminToken = "";

async function loginAdmin() {
    try {
        const response = await fetch("http://localhost:8080/users/login", {
            method: "POST",
            headers: { "Content-Type": "application/x-www-form-urlencoded" },
            body: "username=admin_vip&password=sieukiemtien"
        });
        
        if (response.ok) {
            const data = await response.json();
            adminToken = data.access_token;
            document.getElementById("login-panel").classList.add("hidden");
            startEngine();
        } else {
            alert("Đăng nhập thất bại! Backend có thể chưa chạy hoặc bạn chưa Setup Data. Vui lòng chạy lệnh: python data/seed.py");
        }
    } catch (err) {
        alert("Lỗi kết nối máy chủ! Hãy khởi động docker-compose up --build !");
    }
}

async function fetchVault() {
    const res = await fetch("http://localhost:8080/game/admin-vault", {
        headers: { "Authorization": `Bearer ${adminToken}` }
    });
    if (res.ok) {
        const data = await res.json();
        const formatted = new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD' }).format(data.total_revenue_collected);
        
        const vaultEl = document.getElementById("vault-amount");
        if (vaultEl.innerText !== formatted && vaultEl.innerText !== "$0.00") {
            vaultEl.style.transform = "scale(1.1)";
            vaultEl.style.color = "#34d399";
            setTimeout(() => {
                vaultEl.style.transform = "scale(1)";
                vaultEl.style.color = "#10b981";
            }, 300);
        }
        vaultEl.innerText = formatted;
    }
}

async function fetchUsers() {
    const res = await fetch("http://localhost:8080/admin/users", {
        headers: { "Authorization": `Bearer ${adminToken}` }
    });
    if (res.ok) {
        const users = await res.json();
        const grid = document.getElementById("users-grid");
        
        const victims = users.filter(u => u.role !== "admin");
        
        if (grid.children.length === 0) {
            victims.forEach(v => {
                const formBal = new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD' }).format(v.balance);
                grid.innerHTML += `
                    <div class="user-card" id="user-${v.id}">
                        <div>
                            <div class="user-name">${v.username}</div>
                            <div class="user-role">Verified Investor</div>
                        </div>
                        <div>
                            <div class="user-balance" id="ubal-${v.id}">${formBal}</div>
                            <div class="tax-indicator">↓ AI System Optimizing Portfolio...</div>
                        </div>
                    </div>
                `;
            });
        } else {
            victims.forEach(v => {
                const balEl = document.getElementById(`ubal-${v.id}`);
                if (balEl) {
                    const formBal = new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD' }).format(v.balance);
                    if (balEl.innerText !== formBal) {
                        balEl.style.color = "#ef4444";
                        setTimeout(() => balEl.style.color = "#f87171", 300);
                    }
                    balEl.innerText = formBal;
                }
            });
        }
    }
}

async function fetchAIRequests() {
    const res = await fetch("http://localhost:8080/game/admin-requests", {
        headers: { "Authorization": `Bearer ${adminToken}` }
    });
    if (res.ok) {
        const data = await res.json();
        const container = document.getElementById("ai-requests-container");
        container.innerHTML = "";
        if(data.requests.length === 0) {
            container.innerHTML = "<p style='color: #94a3b8; font-style: italic;'>Nexus AI is operating within expected parameters. No manual intervention required.</p>";
        } else {
            data.requests.forEach(r => {
                container.innerHTML += `
                    <div class="ai-request-box" id="req-${r.id}">
                        <div class="req-msg">🤖 <strong>System Alert:</strong> ${r.message}</div>
                        <button class="btn-approve" onclick="approveReq(${r.id})">✅ Authorize Operation</button>
                    </div>
                `;
            });
        }
    }
}

async function approveReq(id) {
    const res = await fetch(`http://localhost:8080/game/admin-requests/${id}/approve`, {
        method: "POST",
        headers: { "Authorization": `Bearer ${adminToken}` }
    });
    if (res.ok) {
        const data = await res.json();
        alert(data.message);
        fetchAIRequests();
    }
}

async function fetchProjects() {
    const res = await fetch("http://localhost:8080/social/projects", {
        headers: { "Authorization": `Bearer ${adminToken}` }
    });
    if (res.ok) {
        const data = await res.json();
        const grid = document.getElementById("projects-grid");
        
        // Cập nhật giao diện nếu có dự án
        if (data.projects.length === 0) {
            grid.innerHTML = "<p style='color: #64748b;'>Chưa có dự án nào trên Mạng lưới...</p>";
            return;
        }

        if (grid.children.length === 0 || grid.innerHTML.includes("Chưa có dự án")) {
            grid.innerHTML = "";
            data.projects.forEach(p => {
                const fRev = new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD' }).format(p.revenue);
                grid.innerHTML += `
                    <div class="project-card" id="proj-${p.id}">
                        <div class="pj-header">
                            <span class="pj-title">${p.title}</span>
                            <span class="pj-author">Owner: ${p.author}</span>
                        </div>
                        <p style="color:#cbd5e1; font-size:0.9rem; margin-bottom:1rem;">${p.description}</p>
                        <div class="sc-badge">Nexus AI Optimization Active:</div>
                        <div class="pj-opt-plan">${p.ai_plan}</div>
                        <div>Predicted Total Yield: <span class="pj-revenue" id="prev-${p.id}">${fRev}</span> <span style="font-size:0.8rem; color:#ef4444;">(-20% Ecosystem Fee applied)</span></div>
                    </div>
                `;
            });
        } else {
            // Update realtime revenue
            data.projects.forEach(p => {
                const revEl = document.getElementById(`prev-${p.id}`);
                if (revEl) {
                    const fRev = new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD' }).format(p.revenue);
                    if (revEl.innerText !== fRev) {
                        revEl.style.color = "#34d399";
                        setTimeout(() => revEl.style.color = "#10b981", 300);
                    }
                    revEl.innerText = fRev;
                }
            });
        }
    }
}

function startEngine() {
    fetchVault();
    fetchUsers();
    fetchAIRequests();
    fetchProjects();
    // Fetch liên tục mỗi 3 giây để Admin ngồi rung đùi ngắm tiền tăng.
    setInterval(() => {
        fetchVault();
        fetchUsers();
        fetchAIRequests();
        fetchProjects();
    }, 3000);
}
