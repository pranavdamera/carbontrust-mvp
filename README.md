# carbontrust-mvp


# CarbonTrust dApp

## Overview
CarbonTrust is a decentralized application (dApp) for real-time carbon credit verification, leveraging AI-driven biomass estimation and smart contracts on Polygon. It enables project owners—particularly smallholder farmers—to mint, trade, and retire carbon credit NFTs backed by verifiable NDVI-based sequestration data.

## Features
- **AI Model**: Extracts NDVI from Sentinel-2 imagery, trains a PyTorch regression to estimate biomass → CO₂ tonnage.
- **FastAPI Backend**: Provides `/estimate` endpoint for lat/lon & date range to return CO₂ sequestration.
- **Polygon Smart Contract**: ERC-721 NFT minting of carbon credits with metadata (project, location, CO₂, timestamp, verifier).
- **IPFS Storage**: Metadata JSON pinned via Pinata; CID stored in NFT URI.
- **React Dashboard**: Visualize NDVI time series, marketplace table with Buy & Retire actions using ethers.js.
- **Dockerized**: Single-container deployment of FastAPI + dependencies.
- **CI/CD**: GitHub Actions for automated test, lint, and deploy to Render on `main` push.

## Repository Structure
