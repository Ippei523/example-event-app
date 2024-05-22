import { AppBar, Box, Typography } from "@mui/material";

export const Footer = () => {
  return (
    <AppBar
      component="footer"
      position="static"
      className="bg-gray-500 min-h-[140px]"
    >
      <Box className="container mx-auto">
        <Typography className="text-center">© 2021 Event Management</Typography>
      </Box>
    </AppBar>
  );
};
