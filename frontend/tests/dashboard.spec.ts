import { test, expect } from '@playwright/test';

test.describe('StadiumMind AI Dashboard E2E', () => {
  test.beforeEach(async ({ page }) => {
    // Navigate to the base URL (which webServer will spin up on port 5173)
    await page.goto('/');
  });

  test('should load the dashboard and display critical sections', async ({ page }) => {
    // Check main headers
    await expect(page.getByText('StadiumMind AI')).toBeVisible();
    await expect(page.getByText('Operational Command Center')).toBeVisible();

    // Verify operational cards render
    await expect(page.getByRole('region', { name: 'Operational Key Performance Indicators' })).toBeVisible();
    await expect(page.getByText('Transportation Status')).toBeVisible();
    await expect(page.getByText('Accessibility Monitor')).toBeVisible();
    await expect(page.getByText('Sustainability Insights')).toBeVisible();

    // Verify digital twin loads
    await expect(page.locator('#digital-twin-title')).toContainText('Stadium Digital Twin');
  });

  test('should display live incident center updates', async ({ page }) => {
    const incidentCenter = page.locator('section', { hasText: 'Active Incidents' });
    await expect(incidentCenter).toBeVisible();
    
    // Check WCAG aria-labels exist
    const list = page.getByRole('list', { name: 'List of active and resolved incidents' });
    await expect(list).toBeVisible();
    
    // Check for critical incidents
    await expect(page.getByLabel('Severity Critical')).toBeVisible();
  });

  test('should allow interaction with Master Action Plan', async ({ page }) => {
    // Locate the Decision Panel
    const decisionPanel = page.locator('section[aria-labelledby="decision-panel-title"]');
    await expect(decisionPanel).toBeVisible();
    
    // Check explainability text exists
    await expect(page.getByText('Master Action Plan')).toBeVisible();
    
    // Find action button
    const analyzeButton = page.getByRole('button', { name: 'Analyze Current Context' });
    
    // Ensure button is visible and enabled
    await expect(analyzeButton).toBeVisible();
    await expect(analyzeButton).toBeEnabled();
  });
});
