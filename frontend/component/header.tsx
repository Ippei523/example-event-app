import Image from "next/image";
import { AppBar, Button, Toolbar, Typography } from "@mui/material";
import person from "../images/person.svg";

export const Header = () => {
  return (
    <AppBar position="static" className="min-h-[60px]">
      <Toolbar className="flex justify-between items-center">
        {/* 仮の画像が欲しい */}
        <Image src="/logo.svg" alt="logo" width={40} height={40} />
        <Typography variant="h6">イベント管理</Typography>
        <Button color="inherit">
          <Image src={person} alt="person" width={40} height={40} />
        </Button>
      </Toolbar>
    </AppBar>
  );
};
