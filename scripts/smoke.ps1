param(
  [string]$ApiBase = "http://localhost:8000/api/v1"
)

$ErrorActionPreference = "Stop"

Write-Host "[smoke] Checking health endpoint..."
$health = Invoke-RestMethod -Uri "$ApiBase/health" -Method Get
if ($health.status -ne "ok") {
  throw "Health check failed"
}

Write-Host "[smoke] Checking system status endpoint..."
$status = Invoke-RestMethod -Uri "$ApiBase/system/status" -Method Get
if ($status.status -ne "ok") {
  throw "System status check failed"
}

Write-Host "[smoke] Checking capabilities endpoint..."
$caps = Invoke-RestMethod -Uri "$ApiBase/vision/capabilities" -Method Get
if (-not $caps.supports_streaming) {
  throw "Capabilities check failed"
}

Write-Host "[smoke] Running analyze endpoint..."
$analyzePayload = @{ media_type = "image"; prompt = "Smoke test prompt" } | ConvertTo-Json
$analyze = Invoke-RestMethod -Uri "$ApiBase/vision/analyze" -Method Post -ContentType "application/json" -Body $analyzePayload
if (-not $analyze.request_id) {
  throw "Analyze endpoint failed"
}

Write-Host "[smoke] All checks passed."
