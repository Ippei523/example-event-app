import React from "react";
import { Header } from "../component/header";
import { Footer } from "../component/footer";
import { Box } from "@mui/material";

export default function Home() {
  return (
    <main className="relative">
      <Header />
      <Box className="min-h-[calc(100vh-140px-60px)]"></Box>
      <Footer />
    </main>
  );
}
