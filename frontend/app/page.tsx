import React from "react";
import { Header } from "../components/header";
import { Footer } from "../components/footer";
import { Box } from "@mui/material";

export default function Home() {
  return (
    <main className="relative">
      <Header />
      <Box className="min-h-[calc(100vh-70px-60px)]"></Box>
      <Footer />
    </main>
  );
}
