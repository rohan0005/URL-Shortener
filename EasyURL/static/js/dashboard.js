function showQR(qrUrl, shortKey) {
    // Get elements
    const qrImage = document.getElementById('qr-image');
    const placeholder = document.getElementById('qr-placeholder');
    const downloadBtn = document.getElementById('download-btn');
    
    // Update QR image
    qrImage.src = qrUrl;
    qrImage.classList.remove('hidden');
    
    // Hide placeholder
    placeholder.classList.add('hidden');
    
    // Update download button
    downloadBtn.href = qrUrl;
    downloadBtn.download = `qrcode-${shortKey}.png`;
    downloadBtn.classList.remove('hidden');
}

//for eidt button
function enableEdit(shortKey) {
    // hide view ,edit
    document.getElementById(`view-${shortKey}`).classList.add('hidden');
    document.getElementById(`edit-${shortKey}`).classList.remove('hidden');
    
    // showing  Save and Cancel
    document.getElementById(`edit-btn-${shortKey}`).classList.add('hidden');
    document.getElementById(`save-btn-${shortKey}`).classList.remove('hidden');
    document.getElementById(`cancel-btn-${shortKey}`).classList.remove('hidden');
    
    document.getElementById(`edit-${shortKey}`).querySelector('input').focus();
}

// cancel the edit
function cancelEdit(shortKey, originalUrl) {
    
    document.getElementById(`edit-${shortKey}`).querySelector('input').value = originalUrl;
    document.getElementById(`view-${shortKey}`).classList.remove('hidden');
    document.getElementById(`edit-${shortKey}`).classList.add('hidden');
    
    // hide Save and  Cancel
    document.getElementById(`edit-btn-${shortKey}`).classList.remove('hidden');
    document.getElementById(`save-btn-${shortKey}`).classList.add('hidden');
    document.getElementById(`cancel-btn-${shortKey}`).classList.add('hidden');
}

// edit save function
function saveEdit(shortKey) {
    const input = document.getElementById(`input-${shortKey}`);
    const newShortKey = input.value.trim();
    const errorEl = document.getElementById(`error-${shortKey}`);
    
    
    document.getElementById(`edit-${shortKey}`).submit();
}

//delete function

function openDeleteModal(shortKey, shortUrl) {
    document.getElementById('delete-url-display').textContent = shortUrl;
    document.getElementById('delete-form').action = `/delete/${shortKey}/`;
    document.getElementById('delete-modal').classList.remove('hidden');
    document.body.style.overflow = 'hidden';
}

function closeDeleteModal() {
    document.getElementById('delete-modal').classList.add('hidden');
    document.body.style.overflow = 'auto';
}


// stats showing function
function showStats(clicks, expiryDate, isExpired) {
    // hiding  placeholder showing data
    document.getElementById('stats-placeholder').classList.add('hidden');
    document.getElementById('stats-content').classList.remove('hidden');
    
    document.getElementById('stats-clicks').textContent = clicks;
    document.getElementById('stats-expiry').textContent = expiryDate;

    const statusEl = document.getElementById('stats-status');
    const statusCard = document.getElementById('stats-status-card');
    
    if (expiryDate === 'Never') {
        statusEl.textContent = 'Never';
        statusCard.className = 'rounded-xl p-4 text-center bg-blue-100 text-blue-600';
    } else if (isExpired === 'True') {
        statusEl.textContent = '❌ Expired';
        statusCard.className = 'rounded-xl p-4 text-center bg-red-100 text-red-600';
    } else {
        statusEl.textContent = '✅ Active';
        statusCard.className = 'rounded-xl p-4 text-center bg-green-100 text-green-600';
    }
}
