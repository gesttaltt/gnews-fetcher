# Render Deployment Guide

This guide helps you deploy the GNews Fetcher API to Render using Docker.

## Prerequisites

1. **Render Account**: Sign up at [render.com](https://render.com)
2. **GNews API Key**: Get your free token from [gnews.io](https://gnews.io)
3. **GitHub Repository**: Connected to your Render account

## Deployment Steps

### Step 1: Create New Web Service

1. Go to your [Render Dashboard](https://dashboard.render.com)
2. Click **"New +"** → **"Web Service"**
3. Connect your GitHub repository: `gesttaltt/gnews-fetcher`

### Step 2: Configure Service Settings

**Basic Settings:**
- **Name**: `gnews-fetcher` (or your preferred name)
- **Runtime**: **Docker** ⚠️ **IMPORTANT: Choose Docker, not Python**
- **Region**: Choose your preferred region (e.g., Oregon)
- **Branch**: `main`

**Docker Settings:**
- **Dockerfile Path**: `./app/Dockerfile`
- **Docker Context**: `./app`

**Instance Settings:**
- **Plan**: Free (or your preferred plan)

### Step 3: Environment Variables

Add the following environment variable:

| Key | Value | Notes |
|-----|-------|-------|
| `GNEWS_API_KEY` | `your_actual_token_here` | Get from gnews.io |

⚠️ **Security Note**: Never commit API keys to your repository. Always use Render's environment variable feature.

### Step 4: Health Check

- **Health Check Path**: `/`

This endpoint returns the API status and confirms if the API key is configured.

### Step 5: Deploy

1. Click **"Create Web Service"**
2. Render will automatically build and deploy your application
3. Monitor the deployment logs for any issues

## Post-Deployment Testing

Once deployed, your API will be available at: `https://your-service-name.onrender.com`

### Test Endpoints:

1. **Health Check**:
   ```bash
   curl https://your-service-name.onrender.com/
   ```

2. **API Documentation** (Swagger UI):
   ```
   https://your-service-name.onrender.com/docs
   ```

3. **News Endpoint**:
   ```bash
   curl "https://your-service-name.onrender.com/news?query=AI&limit=5"
   ```

## Troubleshooting

### Common Issues:

1. **Build Fails**:
   - Check that Runtime is set to "Docker"
   - Verify Dockerfile Path: `./app/Dockerfile`
   - Verify Docker Context: `./app`

2. **Service Won't Start**:
   - Check that `GNEWS_API_KEY` environment variable is set
   - Check deployment logs for Python/dependency errors

3. **API Returns 502 Errors**:
   - Verify your GNews API key is valid
   - Check the health endpoint first: `/`

### Logs Access:
- View real-time logs in the Render dashboard
- Use logs to debug deployment or runtime issues

## Performance Notes

- **Free Tier**: Service may sleep after 15 minutes of inactivity
- **Cold Starts**: First request after sleep may take 10-30 seconds
- **Upgrade**: Consider paid plans for production use

## Security Best Practices

✅ **Good**:
- Environment variables for secrets
- No API keys in code
- `.gitignore` excludes `.env` files

❌ **Avoid**:
- Hardcoding API keys
- Committing `.env` files
- Exposing sensitive data in logs
