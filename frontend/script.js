document.addEventListener('DOMContentLoaded', () => {

  async function fetchSystemData() {
    try {
      let response = await fetch('/api/system');

      if (!response.ok) {
        throw new Error(`Server returned status: ${response.status}`);
      }

      let rawData = await response.json();
      const data = typeof rawData === 'string' ? JSON.parse(rawData) : rawData;

      renderDashboard(data);

    } catch (error) {
      console.error('Error fetching system details:', error);
      updateStatusStyle('Error');
    }
  }

  function renderDashboard(data) {
    setElementText('hostname', data.hostname);
    setElementText('status-badge', data.status);

    updateStatusStyle(data.status);

    if (data.uptime) {
      const cleanUptime = data.uptime.replace(/^Uptime:\s*/i, '');
      setElementText('uptime', cleanUptime);
    }

    updateMetric('cpu', data.cpu);
    updateMetric('memory', data.memory);
    updateMetric('disk', data.disk);

    setElementText('processes-val', data.processes);
    setElementText('ip-val', data.network?.ip);

    const sshStatus = data.services?.ssh || 'N/A';
    const sshElem = document.getElementById('ssh-val');

    if (sshElem) {
      sshElem.textContent = sshStatus.toUpperCase();
      sshElem.style.color =
        sshStatus.toLowerCase() === 'active' ? '#10b981' : '#ef4444';
    }
  }

  function updateStatusStyle(status) {
    const statusContainer = document.querySelector('.status-indicator');

    if (!statusContainer) return;

    statusContainer.classList.remove(
      'status-healthy',
      'status-warning',
      'status-critical'
    );

    const lowerStatus = (status || '').toLowerCase();

    if (lowerStatus === 'healthy' || lowerStatus === 'ok') {
      statusContainer.classList.add('status-healthy');
    } else if (lowerStatus === 'warning' || lowerStatus === 'degraded') {
      statusContainer.classList.add('status-warning');
    } else {
      statusContainer.classList.add('status-critical');
    }
  }

  function updateMetric(id, rawValue) {
    const numericValue = parseFloat(rawValue) || 0;

    setElementText(`${id}-val`, `${numericValue}%`);

    const barElem = document.getElementById(`${id}-bar`);

    if (barElem) {
      barElem.style.width = `${Math.min(numericValue, 100)}%`;
    }
  }

  function setElementText(id, text) {
    const elem = document.getElementById(id);

    if (elem) {
      elem.textContent = text ?? '--';
    }
  }

  fetchSystemData();

  setInterval(fetchSystemData, 5000);
});
