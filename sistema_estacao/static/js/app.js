const state = {
  readings: [],
  alerts: [],
  thresholds: {},
  activeTab: "dashboard",
};

const cardsConfig = [
  { key: "ph", title: "pH da Agua", unit: "", icon: "activity" },
  { key: "turbidity", title: "Turbidez", unit: "NTU", icon: "waves" },
  { key: "temperature", title: "Temperatura", unit: "degC", icon: "thermometer" },
  { key: "tds", title: "TDS", unit: "ppm", icon: "droplets" },
];

let phChart;
let turbidityChart;

function isOutOfRange(key, value) {
  const t = state.thresholds[key];
  if (!t) return false;

  if (typeof t.min === "number" && value < t.min) return true;
  if (typeof t.max === "number" && value > t.max) return true;
  return false;
}

function mountCharts() {
  const labels = state.readings.map((row) => row.time);

  const phCtx = document.getElementById("ph-chart");
  const turbidityCtx = document.getElementById("turbidity-chart");

  phChart = new Chart(phCtx, {
    type: "line",
    data: {
      labels,
      datasets: [
        {
          label: "pH",
          data: state.readings.map((r) => r.ph),
          borderColor: "#4f46e5",
          borderWidth: 3,
          tension: 0.35,
          fill: false,
          pointRadius: 0,
        },
        {
          label: "Limite Min",
          data: labels.map(() => state.thresholds.ph.min),
          borderColor: "#ef4444",
          borderDash: [6, 4],
          borderWidth: 1,
          pointRadius: 0,
        },
        {
          label: "Limite Max",
          data: labels.map(() => state.thresholds.ph.max),
          borderColor: "#ef4444",
          borderDash: [6, 4],
          borderWidth: 1,
          pointRadius: 0,
        },
      ],
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: { display: false },
      },
    },
  });

  turbidityChart = new Chart(turbidityCtx, {
    type: "line",
    data: {
      labels,
      datasets: [
        {
          label: "Turbidez",
          data: state.readings.map((r) => r.turbidity),
          borderColor: "#f59e0b",
          borderWidth: 3,
          tension: 0.35,
          fill: false,
          pointRadius: 0,
        },
        {
          label: "Limite Max",
          data: labels.map(() => state.thresholds.turbidity.max),
          borderColor: "#ef4444",
          borderDash: [6, 4],
          borderWidth: 1,
          pointRadius: 0,
        },
      ],
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: { display: false },
      },
    },
  });
}

function updateCharts() {
  const labels = state.readings.map((row) => row.time);

  phChart.data.labels = labels;
  phChart.data.datasets[0].data = state.readings.map((r) => r.ph);
  phChart.data.datasets[1].data = labels.map(() => state.thresholds.ph.min);
  phChart.data.datasets[2].data = labels.map(() => state.thresholds.ph.max);
  phChart.update();

  turbidityChart.data.labels = labels;
  turbidityChart.data.datasets[0].data = state.readings.map((r) => r.turbidity);
  turbidityChart.data.datasets[1].data = labels.map(() => state.thresholds.turbidity.max);
  turbidityChart.update();
}

function renderCards() {
  const root = document.getElementById("status-cards");
  const current = state.readings[state.readings.length - 1] || {};

  root.innerHTML = cardsConfig
    .map((cfg) => {
      const value = current[cfg.key] ?? "-";
      const alert = typeof value === "number" && isOutOfRange(cfg.key, value);
      return `
        <article class="card ${alert ? "alert" : ""}" data-sensor="${cfg.key}">
          <div class="card-top">
            <span class="card-title">${cfg.title}</span>
            <span class="card-icon"><i data-lucide="${cfg.icon}"></i></span>
          </div>
          <div>
            <span class="card-value ${alert ? "alert" : ""}">${value}</span><span class="card-unit">${cfg.unit}</span>
          </div>
          ${
            alert
              ? '<div class="card-badge"><i data-lucide="alert-triangle"></i> Fora do limite seguro</div>'
              : ''
          }
        </article>
      `;
    })
    .join("");
}

function renderHistory() {
  const body = document.getElementById("history-body");
  const rows = [...state.readings].reverse();

  body.innerHTML = rows
    .map((row) => {
      const warning =
        isOutOfRange("ph", row.ph) ||
        isOutOfRange("turbidity", row.turbidity) ||
        isOutOfRange("temperature", row.temperature) ||
        isOutOfRange("tds", row.tds);

      return `
      <tr>
        <td>${row.time}</td>
        <td style="color:${isOutOfRange("ph", row.ph) ? "#dc2626" : "inherit"}">${row.ph}</td>
        <td style="color:${isOutOfRange("turbidity", row.turbidity) ? "#dc2626" : "inherit"}">${row.turbidity}</td>
        <td style="color:${isOutOfRange("temperature", row.temperature) ? "#dc2626" : "inherit"}">${row.temperature}</td>
        <td style="color:${isOutOfRange("tds", row.tds) ? "#dc2626" : "inherit"}">${row.tds}</td>
        <td><span class="status ${warning ? "warn" : "ok"}">${warning ? "Anomalia" : "Normal"}</span></td>
      </tr>
      `;
    })
    .join("");
}

function renderAlerts() {
  const root = document.getElementById("alerts-container");
  const dot = document.getElementById("alert-dot");

  dot.classList.toggle("active", state.alerts.length > 0);

  if (!state.alerts.length) {
    root.innerHTML = `
      <div class="empty-alerts">
        <i data-lucide="shield-check"></i>
        <h3>Tudo sob controle</h3>
        <p>Nenhuma anomalia detectada recentemente nos corpos hidricos.</p>
      </div>
    `;
    return;
  }

  root.innerHTML = state.alerts
    .map(
      (alert) => `
      <article class="alert-item ${alert.level}">
        <div class="alert-item-icon"><i data-lucide="alert-triangle"></i></div>
        <div>
          <p class="alert-title">Alerta de ${alert.type}</p>
          <span class="alert-meta">${alert.time}</span>
          <p class="alert-msg">${alert.message}</p>
        </div>
      </article>
    `,
    )
    .join("");
}

function renderAll() {
  renderCards();
  renderHistory();
  renderAlerts();
  lucide.createIcons();
}

function setupTabs() {
  const title = document.getElementById("page-title");
  const exportBtn = document.getElementById("export-btn");

  document.querySelectorAll(".nav-btn").forEach((button) => {
    button.addEventListener("click", () => {
      state.activeTab = button.dataset.tabTarget;

      document.querySelectorAll(".nav-btn").forEach((b) => b.classList.remove("active"));
      button.classList.add("active");

      document.querySelectorAll(".tab-view").forEach((view) => view.classList.remove("active"));
      document.getElementById(`tab-${state.activeTab}`).classList.add("active");

      if (state.activeTab === "dashboard") title.textContent = "Monitoramento em Tempo Real";
      if (state.activeTab === "history") title.textContent = "Historico de Dados";
      if (state.activeTab === "alerts") title.textContent = "Central de Alertas";

      exportBtn.classList.toggle("hidden", state.activeTab !== "history");
    });
  });
}

async function fetchSnapshot() {
  const res = await fetch("/api/snapshot/");
  if (!res.ok) {
    console.error("Falha ao carregar o snapshot inicial");
    return;
  }

  const payload = await res.json();
  state.readings = payload.readings;
  state.alerts = payload.alerts;
  state.thresholds = payload.thresholds;
}

async function tick() {
  const res = await fetch("/api/tick/");
  if (!res.ok) return;
  const payload = await res.json();

  state.readings = payload.readings;
  state.alerts = payload.alerts;

  renderAll();
  updateCharts();
}

async function init() {
  setupTabs();
  await fetchSnapshot();
  renderAll();
  mountCharts();
  setInterval(tick, 5000);
}

init();
