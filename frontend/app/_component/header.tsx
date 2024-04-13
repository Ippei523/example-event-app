import { MenuOutlined } from "@mui/icons-material";
import {
  AppBar,
  Box,
  Button,
  IconButton,
  Toolbar,
  Typography,
} from "@mui/material";

export const Header = () => {
  return (
    <AppBar position="static">
      <Toolbar style={{ display: "flex", justifyContent: "space-between" }}>
        <IconButton edge="start" color="inherit" aria-label="menu">
          <MenuOutlined />
        </IconButton>
        <Typography variant="h6">管理アプリ</Typography>
        <Button color="inherit">Login</Button>
      </Toolbar>
    </AppBar>
  );
};
