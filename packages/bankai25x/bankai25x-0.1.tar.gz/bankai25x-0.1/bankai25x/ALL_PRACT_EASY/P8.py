                        PRACTICAL NO.08
Write the program for the following: 
a. Create a web application for inserting and deleting records from a database
CODE:
ASPX CODE:
<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="WebForm8.aspx.cs" Inherits="WebApplication5.WebForm8" %>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
</head>
<body>
    <form id="form1" runat="server">
        <div>
        </div>
        <asp:Label ID="Label1" runat="server" BorderStyle="Solid" Font-Bold="True" Font-Size="Larger" style="z-index: 1; left: 573px; top: 30px; position: absolute; width: 293px; height: 31px" Text="Database Management"></asp:Label>
       <br /><br />  <br /><br /><br />
        <table align="center">
            <tr>
                <td>RollNo</td>
                <td>
                    <asp:TextBox ID="TextBox1" runat="server"></asp:TextBox></td>
            </tr>
             <tr>
                <td>Name</td>
                <td>
                    <asp:TextBox ID="TextBox2" runat="server"></asp:TextBox></td>
            </tr>
             <tr>
                <td>Age</td>
                <td>
                    <asp:TextBox ID="TextBox3" runat="server"></asp:TextBox></td>
            </tr>
             <tr>
                <td>Class</td>
                <td>
                    <asp:TextBox ID="TextBox4" runat="server"></asp:TextBox></td>
            </tr>
             <tr>
                <td>
                    <asp:Button ID="insert" runat="server" Text="Insert" OnClick="insert_Click" Width="141px" /></td>
                <td>
                    <asp:Button ID="update" runat="server" Text="Delete" OnClick="update_Click" style="margin-left: 33px" Width="149px" /></td>
            </tr>
        </table>
    </form>
</body>
</html>
C# CODE:
using System;
using System.Data;
using System.Data.SqlClient;
namespace WebApplication5
{
    public partial class WebForm8 : System.Web.UI.Page
    {
        SqlConnection con = new SqlConnection(@"Data Source=ROHIT\SQLEXPRESS;Initial Catalog=College; Integrated Security=True");
        protected void Page_Load(object sender, EventArgs e)
        {
        }
        protected void insert_Click(object sender, EventArgs e)
        {
            con.Open();
            SqlCommand cmd = new SqlCommand(@"insert into Student(RollNo,Name,Age,Class)values(
           '"+ Convert.ToInt32(TextBox1.Text)+"','"+TextBox2.Text+ "','" +Convert.ToInt32(TextBox3.Text)+ "','" + TextBox4.Text + "')",con);
             cmd.ExecuteNonQuery(); 
            Response.Write("Data inserted successfully");
            con.Close();
        }
        protected void update_Click(object sender, EventArgs e)
        { 
            con.Open();
            SqlCommand cmd = new SqlCommand("delete from student WHERE RollNo="+ Convert.ToInt32(TextBox1.Text),con);
                cmd.ExecuteNonQuery();
                Console.WriteLine(cmd);         
            Response.Write("Data deleted successfully");
            con.Close();
           
        }
    }
}
OUTPUT:
Insert:

SSMS:






Delete:


SSMS:





b. Create a web application to display Using Disconnected Data Access and Databinding using 
GridView.
CODE:
ASPX CODE:
<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="WebForm8.aspx.cs" Inherits="WebApplication5.WebForm8" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
</head>
<body>
    <form id="form1" runat="server">
        <div>
        </div>
        <asp:Label ID="Label1" runat="server" BorderStyle="Solid" Font-Bold="True" Font-Size="Larger" style="z-index: 1; left: 573px; top: 30px; position: absolute; width: 293px; height: 31px" Text="Database Management"></asp:Label>
       <br /><br />
        <br /><br />
        <br />
        <table align="center">
            <tr>
                <td>Employee ID</td>
                <td>
                    <asp:TextBox ID="TextBox1" runat="server"></asp:TextBox></td>
            </tr>
             <tr>
                <td>Employee Name</td>
                <td>
                    <asp:TextBox ID="TextBox2" runat="server"></asp:TextBox></td>
            </tr>
             <tr>
                <td>Age</td>
                <td>
                    <asp:TextBox ID="TextBox3" runat="server"></asp:TextBox></td>
            </tr>
             <tr>
                <td>Email</td>
                <td>
                    <asp:TextBox ID="TextBox4" runat="server"></asp:TextBox></td>
            </tr>
             <tr>
                <td>
                    <asp:Button ID="insert" runat="server" Text="Insert" OnClick="insert_Click" Width="141px" /></td>
                <td>
                    <asp:Button ID="retrive" runat="server" Text="Retrive" OnClick="update_Click" style="margin-left: 33px" Width="149px" /></td>
            </tr>
        </table>
        <asp:GridView ID="GridView1" runat="server" BackColor="White" BorderColor="White" BorderStyle="Ridge" BorderWidth="2px" CellPadding="3" CellSpacing="1" GridLines="None" style="z-index: 1; left: 412px; top: 383px; position: absolute; height: 180px; width: 330px">
            <FooterStyle BackColor="#C6C3C6" ForeColor="Black" />
            <HeaderStyle BackColor="#4A3C8C" Font-Bold="True" ForeColor="#E7E7FF" />
            <PagerStyle BackColor="#C6C3C6" ForeColor="Black" HorizontalAlign="Right" />
            <RowStyle BackColor="#DEDFDE" ForeColor="Black" />
            <SelectedRowStyle BackColor="#9471DE" Font-Bold="True" ForeColor="White" />
            <SortedAscendingCellStyle BackColor="#F1F1F1" />
            <SortedAscendingHeaderStyle BackColor="#594B9C" />
            <SortedDescendingCellStyle BackColor="#CAC9C9" />
            <SortedDescendingHeaderStyle BackColor="#33276A" />
        </asp:GridView>
    </form>
</body>
</html>


C# CODE:

using System;
using System.Data;
using System.Data.SqlClient;
namespace WebApplication5
{
    public partial class WebForm8 : System.Web.UI.Page
    {
        SqlConnection con = new SqlConnection(@"Data Source=king\SQLEXPRESS;Initial Catalog=College;
                                                    Integrated Security=True");
        protected void Page_Load(object sender, EventArgs e)
        {
        }
        protected void insert_Click(object sender, EventArgs e)
        {
           
            con.Open();
            SqlCommand cmd = new SqlCommand(@"insert into Employee(eid,name,age,email)values(
           '"+ Convert.ToInt32(TextBox1.Text)+"','"+TextBox2.Text+ "','" +Convert.ToInt32(TextBox3.Text)+ "','" + TextBox4.Text + "')",con);
             cmd.ExecuteNonQuery(); 
            Response.Write("Data inserted successfully");
            con.Close();
        }


        protected void update_Click(object sender, EventArgs e)
        { 
            con.Open();
            SqlCommand cmd = new SqlCommand("select *from Employee", con);
            SqlDataAdapter d = new SqlDataAdapter(cmd);
            DataTable dt = new DataTable();
            d.Fill(dt);
            GridView1.DataSource = dt;
            GridView1.DataBind();
            con.Close();
           
        }
    }
}












OUTPUT:



Insert:






Retrieve:

